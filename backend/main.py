from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func
from pydantic import BaseModel
from typing import Optional, List

from database import get_db
from models import Listing


# =========================================================
# CREATE FASTAPI APPLICATION
# =========================================================

app = FastAPI(
    title="Business Listings Dashboard API",
    description="Business Listings Dashboard using React, FastAPI and MySQL",
    version="1.0.0"
)


# =========================================================
# CORS
# Allows React frontend to communicate with FastAPI
# =========================================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# =========================================================
# DATA MODEL / REQUEST SCHEMA
# =========================================================

class ListingCreate(BaseModel):

    business_name: str

    category: Optional[str] = None

    city: Optional[str] = None

    address: Optional[str] = None

    phone: Optional[str] = None

    source: Optional[str] = None


# =========================================================
# HOME
# =========================================================

@app.get("/")
def home():

    return {
        "message": "Business Listings API is running"
    }


# =========================================================
# TEST MYSQL CONNECTION
# =========================================================

@app.get("/test-db")
def test_database(
    db: Session = Depends(get_db)
):

    try:

        count = db.query(Listing).count()

        return {
            "database": "MySQL connected",
            "listing_count": count
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"MySQL connection error: {str(e)}"
        )


# =========================================================
# INSERT ONE BUSINESS LISTING
# =========================================================

@app.post("/listings")
def create_listing(
    listing: ListingCreate,
    db: Session = Depends(get_db)
):

    try:

        new_listing = Listing(
            business_name=listing.business_name,
            category=listing.category,
            city=listing.city,
            address=listing.address,
            phone=listing.phone,
            source=listing.source
        )

        db.add(new_listing)

        db.commit()

        db.refresh(new_listing)

        return {
            "message": "Listing inserted successfully",
            "id": new_listing.id
        }

    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )


# =========================================================
# BULK INSERT
# =========================================================

@app.post("/listings/bulk")
def create_bulk_listings(
    listings: List[ListingCreate],
    db: Session = Depends(get_db)
):

    if not listings:

        raise HTTPException(
            status_code=400,
            detail="No listings provided"
        )

    try:

        new_listings = []

        for listing in listings:

            new_listing = Listing(
                business_name=listing.business_name,
                category=listing.category,
                city=listing.city,
                address=listing.address,
                phone=listing.phone,
                source=listing.source
            )

            new_listings.append(new_listing)

        db.add_all(new_listings)

        db.commit()

        return {
            "message": "Listings inserted successfully",
            "count": len(new_listings)
        }

    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=f"Bulk insert error: {str(e)}"
        )


# =========================================================
# GET ALL LISTINGS
# =========================================================

@app.get("/listings")
def get_listings(
    db: Session = Depends(get_db)
):

    try:

        listings = db.query(Listing).all()

        return listings

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )


# =========================================================
# TOTAL NUMBER OF BUSINESSES
# =========================================================

@app.get("/dashboard/total")
def total_businesses(
    db: Session = Depends(get_db)
):

    try:

        total = db.query(Listing).count()

        return {
            "total_businesses": total
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )


# =========================================================
# CITY-WISE BUSINESS COUNT
# =========================================================

@app.get("/dashboard/city")
def city_count(
    db: Session = Depends(get_db)
):

    try:

        results = (
            db.query(
                Listing.city,
                func.count(Listing.id).label("count")
            )
            .filter(Listing.city.isnot(None))
            .group_by(Listing.city)
            .order_by(
                func.count(Listing.id).desc()
            )
            .all()
        )

        return [
            {
                "city": city,
                "count": count
            }

            for city, count in results
        ]

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"City query error: {str(e)}"
        )


# =========================================================
# CATEGORY-WISE BUSINESS COUNT
# =========================================================

@app.get("/dashboard/category")
def category_count(
    db: Session = Depends(get_db)
):

    try:

        results = (
            db.query(
                Listing.category,
                func.count(Listing.id).label("count")
            )
            .filter(Listing.category.isnot(None))
            .group_by(Listing.category)
            .order_by(
                func.count(Listing.id).desc()
            )
            .all()
        )

        return [
            {
                "category": category,
                "count": count
            }

            for category, count in results
        ]

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Category query error: {str(e)}"
        )


# =========================================================
# SOURCE-WISE BUSINESS COUNT
# =========================================================

@app.get("/dashboard/source")
def source_count(
    db: Session = Depends(get_db)
):

    try:

        results = (
            db.query(
                Listing.source,
                func.count(Listing.id).label("count")
            )
            .filter(Listing.source.isnot(None))
            .group_by(Listing.source)
            .order_by(
                func.count(Listing.id).desc()
            )
            .all()
        )

        return [
            {
                "source": source,
                "count": count
            }

            for source, count in results
        ]

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Source query error: {str(e)}"
        )