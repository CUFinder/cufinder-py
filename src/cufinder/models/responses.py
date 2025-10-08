"""API response models."""

from typing import List, Optional

from .base import BaseModel
from .company import Company
from .person import Person


class CufResponse(BaseModel):
    """Response model for CUF (Company URL Finder) API."""
    
    domain: Optional[str] = None
    company_name: Optional[str] = None
    country_code: Optional[str] = None
    confidence: Optional[float] = None
    status: Optional[str] = None
    message: Optional[str] = None


class EppResponse(BaseModel):
    """Response model for EPP (Email Pattern Predictor) API."""
    
    person: Optional[Person] = None
    company: Optional[Company] = None
    linkedin_url: Optional[str] = None
    confidence: Optional[float] = None
    status: Optional[str] = None
    message: Optional[str] = None


class LbsResponse(BaseModel):
    """Response model for LBS (Local Business Search) API."""
    
    businesses: Optional[List[dict]] = None
    total: Optional[int] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
    status: Optional[str] = None
    message: Optional[str] = None


class DtcResponse(BaseModel):
    """Response model for DTC (Domain to Company Name) API."""
    
    company_name: Optional[str] = None
    company_website: Optional[str] = None
    confidence: Optional[float] = None
    status: Optional[str] = None
    message: Optional[str] = None


class DteResponse(BaseModel):
    """Response model for DTE (Company Email Finder) API."""
    
    emails: Optional[List[str]] = None
    company_website: Optional[str] = None
    confidence: Optional[float] = None
    status: Optional[str] = None
    message: Optional[str] = None


class NtpResponse(BaseModel):
    """Response model for NTP (Company Phone Finder) API."""
    
    phones: Optional[List[str]] = None
    company_name: Optional[str] = None
    confidence: Optional[float] = None
    status: Optional[str] = None
    message: Optional[str] = None


class RelResponse(BaseModel):
    """Response model for REL (Reverse Email Lookup) API."""
    
    person: Optional[Person] = None
    company: Optional[Company] = None
    email: Optional[str] = None
    confidence: Optional[float] = None
    status: Optional[str] = None
    message: Optional[str] = None


class FclResponse(BaseModel):
    """Response model for FCL (Company Lookalikes Finder) API."""
    
    lookalikes: Optional[List[dict]] = None
    query: Optional[str] = None
    total: Optional[int] = None
    status: Optional[str] = None
    message: Optional[str] = None


class ElfResponse(BaseModel):
    """Response model for ELF (Company Fundraising) API."""
    
    fundraising: Optional[dict] = None
    query: Optional[str] = None
    confidence: Optional[float] = None
    status: Optional[str] = None
    message: Optional[str] = None


class CarResponse(BaseModel):
    """Response model for CAR (Company Revenue Finder) API."""
    
    revenue: Optional[str] = None
    query: Optional[str] = None
    confidence: Optional[float] = None
    status: Optional[str] = None
    message: Optional[str] = None


class FccResponse(BaseModel):
    """Response model for FCC (Company Subsidiaries Finder) API."""
    
    subsidiaries: Optional[List[dict]] = None
    query: Optional[str] = None
    total: Optional[int] = None
    status: Optional[str] = None
    message: Optional[str] = None


class FtsResponse(BaseModel):
    """Response model for FTS (Company Tech Stack Finder) API."""
    
    tech_stack: Optional[List[str]] = None
    query: Optional[str] = None
    confidence: Optional[float] = None
    status: Optional[str] = None
    message: Optional[str] = None


class FweResponse(BaseModel):
    """Response model for FWE (Email from Profile) API."""
    
    email: Optional[str] = None
    profile_url: Optional[str] = None
    confidence: Optional[float] = None
    status: Optional[str] = None
    message: Optional[str] = None


class TepResponse(BaseModel):
    """Response model for TEP (Person Enrichment) API."""
    
    person: Optional[Person] = None
    query: Optional[str] = None
    confidence: Optional[float] = None
    status: Optional[str] = None
    message: Optional[str] = None


class EncResponse(BaseModel):
    """Response model for ENC (Company Enrichment) API."""
    
    company: Optional[Company] = None
    query: Optional[str] = None
    confidence: Optional[float] = None
    status: Optional[str] = None
    message: Optional[str] = None


class CecResponse(BaseModel):
    """Response model for CEC (Company Employee Countries) API."""
    
    countries: Optional[List[str]] = None
    query: Optional[str] = None
    total: Optional[int] = None
    status: Optional[str] = None
    message: Optional[str] = None


class CloResponse(BaseModel):
    """Response model for CLO (Company Locations) API."""
    
    locations: Optional[List[dict]] = None
    query: Optional[str] = None
    total: Optional[int] = None
    status: Optional[str] = None
    message: Optional[str] = None


class CseResponse(BaseModel):
    """Response model for CSE (Company Search) API."""
    
    companies: Optional[List[dict]] = None
    total: Optional[int] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
    status: Optional[str] = None
    message: Optional[str] = None


class PseResponse(BaseModel):
    """Response model for PSE (People Search) API."""
    
    people: Optional[List[dict]] = None
    total: Optional[int] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
    status: Optional[str] = None
    message: Optional[str] = None


class LcufResponse(BaseModel):
    """Response model for LCUF (LinkedIn Company URL Finder) API."""
    
    linkedin_url: Optional[str] = None
    company_name: Optional[str] = None
    confidence: Optional[float] = None
    status: Optional[str] = None
    message: Optional[str] = None
