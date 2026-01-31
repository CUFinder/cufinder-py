# Cufinder Python SDK Changelog

## 1.1.0 (January 31, 2025)

#### Features
- **New V2 API services**: Add new V2 services including `BCD`, `CCP`, `ISC`, `CBC`, `CSC`, `CSN`, `NAO` and `NAA`


#### Documentation
- **Updated README.md**: Add API reference for all new services


## 1.0.0 (November 4, 2025)

#### Documentation
- Updated all service method examples with correct SDK usage patterns
- Fixed inline code examples across all 20 services (CUF, LCUF, DTC, DTE, NTP, REL, FCL, ELF, CAR, FCC, FTS, EPP, FWE, TEP, ENC, CEC, CLO, CSE, PSE, LBS)
- Improved docstrings with detailed parameter descriptions and working examples
- Added realistic examples using actual company names
- Ensured all examples use correct response field names and SDK convenience methods
- Updated all service examples to use `client.service_name()`

#### Bug Fixes
- Fixed parsing results from API responses for all services and improve error handling



## 0.1.0 (October 9, 2025)

#### Features
- Initial release of the Cufinder Python SDK
- Implemented CUF (Company URL Finder) service for finding company domains
- Implemented EPP (Email Pattern Predictor) service for LinkedIn profile enrichment
- Implemented LBS (Local Business Search) service for local business discovery
- Added comprehensive type safety with Pydantic models
- Implemented robust error handling with specific exception types
- Added retry logic and timeout configuration
- Created extensive documentation and examples

#### Architecture
- Built with modern Python practices and type hints
- Follows SOLID principles for maintainable code
- Uses Pydantic for data validation and serialization
- Implements proper separation of concerns between client, services, and models
- Added comprehensive test coverage

#### Developer Experience
- Simple and intuitive API design
- Extensive documentation with examples
- Type-safe responses with IDE support
- Configurable timeouts and retry logic
- Production-ready error handling



## 0.0.1 (October 8, 2025)

Initial release of the Cufinder Python SDK with core functionality.
