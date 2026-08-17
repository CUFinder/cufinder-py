"""Tests for the Cufinder SDK."""

import pytest
from unittest.mock import Mock, patch

from cufinder import Cufinder
from cufinder.exceptions import ValidationError, AuthenticationError


class TestCufinder:
    """Test cases for Cufinder."""

    def test_init_with_valid_api_key(self):
        """Test SDK initialization with valid API key."""
        sdk = Cufinder(api_key="test-key")
        assert sdk.client.api_key == "test-key"
        assert sdk.client.base_url == "https://api.cufinder.io/v2"

    def test_init_with_custom_config(self):
        """Test SDK initialization with custom configuration."""
        sdk = Cufinder(
            api_key="test-key",
            base_url="https://custom.api.com",
            timeout=60,
            max_retries=5
        )
        assert sdk.client.base_url == "https://custom.api.com"
        assert sdk.client.timeout == 60
        assert sdk.client.max_retries == 5

    def test_get_client(self):
        """Test getting the underlying client."""
        sdk = Cufinder(api_key="test-key")
        client = sdk.get_client()
        assert client.api_key == "test-key"

    @patch('cufinder.base_api_client.requests.Session')
    def test_cuf_service(self, mock_session):
        """Test CUF service method."""
        # Mock response
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
            "query": "test",
            "credit_count": 1,
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.cuf("TechCorp", "US")

        assert result.domain == "techcorp.com"
        assert result.company_name == "TechCorp"
        assert result.confidence == 0.95

    @patch('cufinder.base_api_client.requests.Session')
    def test_epp_service(self, mock_session):
        """Test EPP service method."""
        # Mock response
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
            "query": "test",
            "credit_count": 1,
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.epp("https://linkedin.com/in/johndoe")

        assert result.person.full_name == "John Doe"
        assert result.person.job_title == "Software Engineer"
        assert result.company.name == "TechCorp"
        assert result.confidence == 0.90

    @patch('cufinder.base_api_client.requests.Session')
    def test_lbs_service(self, mock_session):
        """Test LBS service method."""
        # Mock response
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
            "query": "test",
            "credit_count": 1,
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.lbs(name="coffee", city="San Francisco")

        assert len(result.businesses) == 2
        assert result.total_results == 2
        assert result.businesses[0]["name"] == "Coffee Shop"

    @patch('cufinder.base_api_client.requests.Session')
    def test_dtc_service(self, mock_session):
        """Test DTC service method."""
        # Mock response
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
            "query": "test",
            "credit_count": 1,
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.dtc("https://example.com")

        assert result.company_name == "Example Corp"
        assert result.company_website == "https://example.com"
        assert result.confidence == 0.85

    @patch('cufinder.base_api_client.requests.Session')
    def test_dte_service(self, mock_session):
        """Test DTE service method."""
        # Mock response
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
            "query": "test",
            "credit_count": 1,
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.dte("https://example.com")

        assert len(result.emails) == 2
        assert "contact@example.com" in result.emails
        assert result.confidence == 0.80

    @patch('cufinder.base_api_client.requests.Session')
    def test_ntp_service(self, mock_session):
        """Test NTP service method."""
        # Mock response
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
            "query": "test",
            "credit_count": 1,
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.ntp("TechCorp")

        assert len(result.phones) == 2
        assert "+1-555-123-4567" in result.phones
        assert result.company_name == "TechCorp"

    @patch('cufinder.base_api_client.requests.Session')
    def test_rel_service(self, mock_session):
        """Test REL service method."""
        # Mock response
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
            "query": "test",
            "credit_count": 1,
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.rel("jane@example.com")

        assert result.person.full_name == "Jane Smith"
        assert result.person.email == "jane@example.com"
        assert result.company.name == "Example Corp"
        assert result.confidence == 0.88

    @patch('cufinder.base_api_client.requests.Session')
    def test_fcl_service(self, mock_session):
        """Test FCL service method."""
        # Mock response
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.fcl("TechCorp")

        assert len(result.companies) == 2
        assert result.total == 2
        assert result.companies[0]["name"] == "SimilarCorp"

    @patch('cufinder.base_api_client.requests.Session')
    def test_elf_service(self, mock_session):
        """Test ELF service method."""
        # Mock response
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.elf("TechCorp")

        assert result.fundraising["total_raised"] == "$10M"
        assert len(result.fundraising["rounds"]) == 2
        assert result.confidence == 0.82

    @patch('cufinder.base_api_client.requests.Session')
    def test_car_service(self, mock_session):
        """Test CAR service method."""
        # Mock response
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.car("TechCorp")

        assert result.revenue == "$50M - $100M"
        assert result.query == "TechCorp"
        assert result.confidence == 0.75

    @patch('cufinder.base_api_client.requests.Session')
    def test_fcc_service(self, mock_session):
        """Test FCC service method."""
        # Mock response
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.fcc("Alphabet Inc")

        assert len(result.subsidiaries) == 2
        assert result.total == 2
        assert result.subsidiaries[0]["name"] == "SubCorp1"

    @patch('cufinder.base_api_client.requests.Session')
    def test_fts_service(self, mock_session):
        """Test FTS service method."""
        # Mock response
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.fts("TechCorp")

        assert len(result.tech_stack) == 4
        assert "Python" in result.tech_stack
        assert "React" in result.tech_stack
        assert result.confidence == 0.90

    @patch('cufinder.base_api_client.requests.Session')
    def test_fwe_service(self, mock_session):
        """Test FWE service method."""
        # Mock response
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
            "query": "test",
            "credit_count": 1,
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.fwe("https://linkedin.com/in/johndoe")

        assert result.work_email == "john.doe@example.com"
        assert result.profile_url == "https://linkedin.com/in/johndoe"
        assert result.confidence == 0.85

    @patch('cufinder.base_api_client.requests.Session')
    def test_tep_service(self, mock_session):
        """Test TEP service method."""
        # Mock response
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.tep("John Doe", "TechCorp")

        assert result.person.full_name == "John Doe"
        assert result.person.job_title == "Software Engineer"
        assert result.person.company == "TechCorp"
        assert result.confidence == 0.88

    @patch('cufinder.base_api_client.requests.Session')
    def test_enc_service(self, mock_session):
        """Test ENC service method."""
        # Mock response
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.enc("TechCorp")

        assert result.company.name == "TechCorp Inc"
        assert result.company.industry == "Technology"
        assert result.company.size == "100-500"
        assert result.confidence == 0.92

    @patch('cufinder.base_api_client.requests.Session')
    def test_cec_service(self, mock_session):
        """Test CEC service method."""
        # Mock response
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.cec("TechCorp")

        assert len(result.countries) == 3
        assert "United States" in result.countries
        assert "Canada" in result.countries
        assert result.total == 3

    @patch('cufinder.base_api_client.requests.Session')
    def test_clo_service(self, mock_session):
        """Test CLO service method."""
        # Mock response
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.clo("TechCorp")

        assert len(result.locations) == 2
        assert result.locations[0]["city"] == "San Francisco"
        assert result.total == 2

    @patch('cufinder.base_api_client.requests.Session')
    def test_cse_service(self, mock_session):
        """Test CSE service method."""
        # Mock response
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
            "query": "test",
            "credit_count": 1,
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.cse(name="tech", industry="software")

        assert len(result.companies) == 2
        assert result.total_results == 2
        assert result.companies[0]["name"] == "TechCorp"

    @patch('cufinder.base_api_client.requests.Session')
    def test_pse_service(self, mock_session):
        """Test PSE service method."""
        # Mock response
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
            "query": "test",
            "credit_count": 1,
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.pse(full_name="engineer", company_name="TechCorp")

        assert len(result.people) == 2
        assert result.total_results == 2
        assert result.people[0]["name"] == "John Doe"

    @patch('cufinder.base_api_client.requests.Session')
    def test_lcuf_service(self, mock_session):
        """Test LCUF service method."""
        # Mock response
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
            "query": "test",
            "credit_count": 1,
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.lcuf("TechCorp")

        assert result.linkedin_url == "https://linkedin.com/company/techcorp"
        assert result.company_name == "TechCorp"
        assert result.confidence == 0.95

    @patch('cufinder.base_api_client.requests.Session')
    def test_psa_service(self, mock_session):
        """Test PSA service method."""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.psa(signal_name="employee_growth", time_frame=90, bucket="high", page=1)

        assert len(result.contacts) == 1
        assert result.contacts[0].full_name == "John Doe"
        assert result.contacts[0].current_job["title"] == "Software Engineer"
        assert result.contacts[0].company["name"] == "TechCorp"
        assert result.contacts[0].signal.name == "employee_growth"
        assert result.contacts[0].signal.time_frame == 90
        assert result.contacts[0].signal.bucket == "high"
        assert result.credit_count == 1

    @patch('cufinder.base_api_client.requests.Session')
    def test_csa_service(self, mock_session):
        """Test CSA service method."""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.csa(signal_name="employee_growth", time_frame=90, bucket="high", page=1)

        assert len(result.companies) == 1
        assert result.companies[0].name == "TechCorp"
        assert result.companies[0].domain == "techcorp.com"
        assert result.companies[0].employees["range"] == "1001-5000"
        assert result.companies[0].signal.name == "employee_growth"
        assert result.companies[0].signal.bucket == "high"
        assert result.credit_count == 1

    @patch('cufinder.base_api_client.requests.Session')
    def test_jca_service(self, mock_session):
        """Test JCA service method."""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.jca(start_date="2026-01-01", end_date="2026-08-16", type="promotion")

        assert len(result.job_changes) == 1
        assert result.job_changes[0].type == "promotion"
        assert result.job_changes[0].from_.company_name == "TechCorp"
        assert result.job_changes[0].from_.title == "Software Engineer"
        assert result.job_changes[0].to.title == "Senior Software Engineer"
        assert result.credit_count == 1

    @patch('cufinder.base_api_client.requests.Session')
    def test_clf_service(self, mock_session):
        """Test CLF service method."""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
            "query": "linkedin.com/in/mortezaheydari1997",
            "profiles": [
                {
                    "full_name": "Morteza Heydari",
                    "linkedin_url": "https://linkedin.com/in/mortezaheydari1997",
                    "job_title": "Founder & CEO",
                    "company_name": "CUFinder",
                    "languages": [
                        {"name": "türkçe", "proficiency": "-"},
                        {"name": "i̇ngilizce", "proficiency": "-"},
                    ],
                }
            ],
            "credit_count": 1,
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.clf(query="linkedin.com/in/mortezaheydari1997")

        assert len(result.profiles) == 1
        assert result.profiles[0].full_name == "Morteza Heydari"
        assert result.profiles[0].linkedin_url == "https://linkedin.com/in/mortezaheydari1997"
        assert result.profiles[0].job_title == "Founder & CEO"
        assert result.profiles[0].company_name == "CUFinder"
        assert result.profiles[0].languages[0]["name"] == "türkçe"
        assert result.profiles[0].languages[1]["proficiency"] == "-"
        assert result.credit_count == 1

    @patch('cufinder.base_api_client.requests.Session')
    def test_nap_service(self, mock_session):
        """Test NAP service method."""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.nap("morteza heydari")

        assert result.normalized_name == "Morteza Heydari"
        assert result.credit_count == 1

    @patch('cufinder.base_api_client.requests.Session')
    def test_nau_service(self, mock_session):
        """Test NAU service method."""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.nau("https://www.cufinder.io/about-us")

        assert result.normalized_url == "https://www.cufinder.io/about-us"
        assert result.credit_count == 1

    @patch('cufinder.base_api_client.requests.Session')
    def test_gdc_service(self, mock_session):
        """Test GDC service method."""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.gdc("https://www.stripe.com")

        assert result.offers_demo == "yes"
        assert result.credit_count == 1

    @patch('cufinder.base_api_client.requests.Session')
    def test_cot_service(self, mock_session):
        """Test COT service method."""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.headers = {}
        mock_response.json.return_value = {
        }
        mock_session.return_value.request.return_value = mock_response

        sdk = Cufinder(api_key="test-key")
        result = sdk.cot("https://www.stripe.com")

        assert result.offers_free_trial == "yes"
        assert result.credit_count == 1
