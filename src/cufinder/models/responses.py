"""API response models."""

from typing import List, Optional, Union

from .base import BaseModel, BaseResponse
from .company import Company, CompanySearchResult, LocalBusinessResult, LookalikeCompany, FundraisingInfo, CloCompanyLocation, SnapshotModel, Signal, ContactSignal
from .person import Person, PersonSearchResult, TepPerson, CefEmployee


class CufResponse(BaseResponse):
    """CUF Response - Company Name to Domain"""
    domain: str


class LcufResponse(BaseResponse):
    """LCUF Response - Company LinkedIn URL Finder"""
    linkedin_url: str


class DtcResponse(BaseResponse):
    """DTC Response - Domain to Company Name"""
    company_name: str


class DteResponse(BaseResponse):
    """DTE Response - Company Email Finder"""
    emails: List[str]


class NtpResponse(BaseResponse):
    """NTP Response - Company Phone Finder"""
    phones: List[str]


class RelResponse(BaseResponse):
    """REL Response - Reverse Email Lookup"""
    person: Person


class FclResponse(BaseResponse):
    """FCL Response - Company Lookalikes Finder"""
    companies: List[LookalikeCompany]


class ElfResponse(BaseResponse):
    """ELF Response - Company Fundraising API"""
    fundraising_info: FundraisingInfo


class CarResponse(BaseResponse):
    """CAR Response - Company Revenue Finder"""
    annual_revenue: str


class FccResponse(BaseResponse):
    """FCC Response - Company Subsidiaries Finder"""
    subsidiaries: List[str]


class FtsResponse(BaseResponse):
    """FTS Response - Company Tech Stack Finder"""
    technologies: List[str]


class EppResponse(BaseResponse):
    """EPP Response - LinkedIn Profile Enrichment"""
    person: Person


class FweResponse(BaseResponse):
    """FWE Response - LinkedIn Profile Email Finder"""
    work_email: str


class TepResponse(BaseResponse):
    """TEP Response - Person Enrichment"""
    person: TepPerson


class EncResponse(BaseResponse):
    """ENC Response - Company Enrichment"""
    company: Company


class CecResponse(BaseResponse):
    """CEC Response - Company Employees Countries"""
    countries: Union[dict, list]


class CloResponse(BaseResponse):
    """CLO Response - Company Locations"""
    locations: List[CloCompanyLocation]


class CseResponse(BaseResponse):
    """CSE Response - Company Search"""
    companies: List[CompanySearchResult]


class PseResponse(BaseResponse):
    """PSE Response - Person Search"""
    peoples: List[PersonSearchResult]


class LbsResponse(BaseResponse):
    """LBS Response - Local Business Search"""
    companies: List[LocalBusinessResult]


class BcdResponse(BaseResponse):
    """BCD Response - Extract B2B Customers From the Domain"""
    customers: List[str]


class CcpResponse(BaseResponse):
    careers_page_url: str | None


class IscResponse(BaseResponse):
    is_saas: str


class CbcResponse(BaseResponse):
    business_type: str


class CscResponse(BaseResponse):
    mission_statement: str | None


class CsnResponse(BaseResponse):
    company_snapshot: SnapshotModel


class NaoResponse(BaseResponse):
    phone: str


class NaaResponse(BaseResponse):
    address: str


class CefResponse(BaseResponse):
    """CEF Response - Company Employee Finder"""
    employees: List[CefEmployee]


class NacResponse(BaseResponse):
    """NAC Response - Company Name Normalizer"""
    company: str


class CaaActivity(BaseModel):
    """CAA Activity model"""
    activity_url: Optional[str] = None
    activity_id: Optional[str] = None
    author_name: Optional[str] = None
    author_type: Optional[str] = None
    author_url: Optional[str] = None
    activity_comments_count: Optional[int] = None
    activity_hashtags: Optional[List[str]] = None
    activity_headline: Optional[str] = None
    activity_images: Optional[List[str]] = None
    activity_is_video: Optional[bool] = None
    activity_posted_at: Optional[str] = None
    activity_reactions_count: Optional[int] = None
    activity_reposts_count: Optional[int] = None
    activity_text: Optional[str] = None
    activity_top_comments: Optional[List[str]] = None
    activity_videos: Optional[List[str]] = None


class CaaResponse(BaseResponse):
    """CAA Response - Company Activity API"""
    activities: List[CaaActivity]


class CjaCompany(BaseModel):
    """CJA Company model"""
    name: Optional[str] = None
    industry: Optional[str] = None
    website: Optional[str] = None
    linkedin: Optional[str] = None
    followers_count: Optional[int] = None
    employees: Optional[dict] = None
    founded_date: Optional[str] = None
    annual_revenue: Optional[str] = None
    funding_amount: Optional[str] = None
    main_location: Optional[dict] = None


class CjaJob(BaseModel):
    """CJA Job model"""
    job_id: Optional[str] = None
    title: Optional[str] = None
    url: Optional[str] = None
    location: Optional[str] = None
    posted_at: Optional[str] = None
    posted_at_text: Optional[str] = None


class CjaJobItem(BaseModel):
    """CJA Job Item model"""
    company: CjaCompany
    job: CjaJob


class CjaResponse(BaseResponse):
    """CJA Response - Company Jobs API"""
    jobs: List[CjaJobItem]


class PsaResponse(BaseResponse):
    """PSA Response - Contact Signals API"""
    contacts: List[ContactSignal]
