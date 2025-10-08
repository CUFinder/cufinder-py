"""Main Cufinder SDK class."""

from typing import Optional

from .client import CUFinderClient
from .services import (
    Cuf, Epp, Lbs, Dtc, Dte, Ntp, Rel, Fcl, Elf, Car, Fcc, Fts, Fwe, Tep, Enc, Cec, Clo, Cse, Pse, Lcuf
)


class CufinderSDK:
    """
    Main CUFinder SDK class.
    
    Provides access to all API services as direct methods.
    Usage: sdk.cuf(company_name="TechCorp", country_code="US")
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.cufinder.io/v2",
        timeout: int = 30,
        max_retries: int = 3,
    ):
        """
        Initialize the Cufinder SDK.
        
        Args:
            api_key: Your Cufinder API key
            base_url: Base URL for the API (default: https://api.cufinder.io/v2)
            timeout: Request timeout in seconds (default: 30)
            max_retries: Maximum number of retries for failed requests (default: 3)
        """
        self.client = CUFinderClient(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
        )

        # Initialize service instances
        self._cuf = Cuf(self.client)
        self._epp = Epp(self.client)
        self._lbs = Lbs(self.client)
        self._dtc = Dtc(self.client)
        self._dte = Dte(self.client)
        self._ntp = Ntp(self.client)
        self._rel = Rel(self.client)
        self._fcl = Fcl(self.client)
        self._elf = Elf(self.client)
        self._car = Car(self.client)
        self._fcc = Fcc(self.client)
        self._fts = Fts(self.client)
        self._fwe = Fwe(self.client)
        self._tep = Tep(self.client)
        self._enc = Enc(self.client)
        self._cec = Cec(self.client)
        self._clo = Clo(self.client)
        self._cse = Cse(self.client)
        self._pse = Pse(self.client)
        self._lcuf = Lcuf(self.client)

    # Company Services
    def cuf(self, company_name: str, country_code: str):
        """
        Get company domain from company name.
        
        Args:
            company_name: The name of the company
            country_code: ISO 3166-1 alpha-2 country code (e.g., 'US', 'GB')
            
        Returns:
            CufResponse: Company domain information
        """
        return self._cuf.get_domain(company_name, country_code)

    def dtc(self, company_website: str):
        """
        Get company name from domain.
        
        Args:
            company_website: The website URL to lookup
            
        Returns:
            DtcResponse: Company name information
        """
        return self._dtc.get_company_name(company_website)

    def dte(self, company_website: str):
        """
        Get company emails from domain.
        
        Args:
            company_website: The website URL to find emails for
            
        Returns:
            DteResponse: Company email information
        """
        return self._dte.get_emails(company_website)

    def ntp(self, company_name: str):
        """
        Get company phones from company name.
        
        Args:
            company_name: The name of the company to find phones for
            
        Returns:
            NtpResponse: Company phone information
        """
        return self._ntp.get_phones(company_name)

    def lcuf(self, company_name: str):
        """
        Get LinkedIn URL from company name.
        
        Args:
            company_name: The name of the company to find LinkedIn URL for
            
        Returns:
            LcufResponse: LinkedIn URL information
        """
        return self._lcuf.get_linkedin_url(company_name)

    # Person Services
    def epp(self, linkedin_url: str):
        """
        Enrich LinkedIn profile.
        
        Args:
            linkedin_url: The LinkedIn profile URL to enrich
            
        Returns:
            EppResponse: Enriched person and company data
        """
        return self._epp.enrich_profile(linkedin_url)

    def rel(self, email: str):
        """
        Reverse email lookup.
        
        Args:
            email: The email address to lookup
            
        Returns:
            RelResponse: Person and company information
        """
        return self._rel.reverse_email_lookup(email)

    def fwe(self, profile_url: str):
        """
        Get email from profile.
        
        Args:
            profile_url: Social media profile URL to extract email from
            
        Returns:
            FweResponse: Email information
        """
        return self._fwe.get_email_from_profile(profile_url)

    def tep(self, query: str):
        """
        Enrich person information.
        
        Args:
            query: Person name, email, or other identifier to enrich
            
        Returns:
            TepResponse: Enriched person information
        """
        return self._tep.enrich_person(query)

    # Company Intelligence Services
    def fcl(self, query: str):
        """
        Get company lookalikes.
        
        Args:
            query: Company name or description to find similar companies for
            
        Returns:
            FclResponse: List of similar companies
        """
        return self._fcl.get_lookalikes(query)

    def elf(self, query: str):
        """
        Get company fundraising information.
        
        Args:
            query: Company name to get fundraising data for
            
        Returns:
            ElfResponse: Fundraising information
        """
        return self._elf.get_fundraising(query)

    def car(self, query: str):
        """
        Get company revenue.
        
        Args:
            query: Company name to get revenue data for
            
        Returns:
            CarResponse: Revenue information
        """
        return self._car.get_revenue(query)

    def fcc(self, query: str):
        """
        Get company subsidiaries.
        
        Args:
            query: Company name to find subsidiaries for
            
        Returns:
            FccResponse: Subsidiaries information
        """
        return self._fcc.get_subsidiaries(query)

    def fts(self, query: str):
        """
        Get company tech stack.
        
        Args:
            query: Company name or website to get tech stack for
            
        Returns:
            FtsResponse: Technology stack information
        """
        return self._fts.get_tech_stack(query)

    def enc(self, query: str):
        """
        Enrich company information.
        
        Args:
            query: Company name or domain to enrich
            
        Returns:
            EncResponse: Enriched company information
        """
        return self._enc.enrich_company(query)

    def cec(self, query: str):
        """
        Get company employee countries.
        
        Args:
            query: Company name to get employee countries for
            
        Returns:
            CecResponse: Employee countries information
        """
        return self._cec.get_employee_countries(query)

    def clo(self, query: str):
        """
        Get company locations.
        
        Args:
            query: Company name to get locations for
            
        Returns:
            CloResponse: Company locations information
        """
        return self._clo.get_locations(query)

    # Search Services
    def lbs(
        self,
        name: Optional[str] = None,
        country: Optional[str] = None,
        state: Optional[str] = None,
        city: Optional[str] = None,
        industry: Optional[str] = None,
        page: Optional[int] = None,
    ):
        """
        Search local businesses.
        
        Args:
            name: Business name to search for
            country: Country to search in
            state: State/Province to search in
            city: City to search in
            industry: Industry to filter by
            page: Page number for pagination
            
        Returns:
            LbsResponse: Local business search results
        """
        return self._lbs.search_local_businesses(
            name=name,
            country=country,
            state=state,
            city=city,
            industry=industry,
            page=page,
        )

    def cse(
        self,
        query: Optional[str] = None,
        industry: Optional[str] = None,
        location: Optional[str] = None,
        size: Optional[str] = None,
        page: Optional[int] = None,
    ):
        """
        Search companies.
        
        Args:
            query: Company name or description to search for
            industry: Industry to filter by
            location: Location to filter by
            size: Company size to filter by
            page: Page number for pagination
            
        Returns:
            CseResponse: Company search results
        """
        return self._cse.search_companies(
            query=query,
            industry=industry,
            location=location,
            size=size,
            page=page,
        )

    def pse(
        self,
        query: Optional[str] = None,
        job_title: Optional[str] = None,
        company: Optional[str] = None,
        location: Optional[str] = None,
        page: Optional[int] = None,
    ):
        """
        Search people.
        
        Args:
            query: Person name or description to search for
            job_title: Job title to filter by
            company: Company to filter by
            location: Location to filter by
            page: Page number for pagination
            
        Returns:
            PseResponse: People search results
        """
        return self._pse.search_people(
            query=query,
            job_title=job_title,
            company=company,
            location=location,
            page=page,
        )

    def get_client(self) -> CUFinderClient:
        """
        Get the underlying HTTP client for advanced usage.
        
        Returns:
            CUFinderClient: The CUFinderClient instance
        """
        return self.client

