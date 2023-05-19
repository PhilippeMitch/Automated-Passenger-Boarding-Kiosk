In this step, we combined all the extracted data from various sources in previous steps and create the final validation results that as been described at the start of this project which are:

* Passenger name validation (NameValidation)
* Passenger date of birth validation (DoBValidation)
* Passenger face validation (PersonValidation)
* Passenger flight details validation (BoardingPassValidation)
* Passenger carry-on baggage validation for lighter detection (LuggageValidation)


The initial validation status values are set to FALSE in the flight manifest table before performing any validation.
To perform the validation process we combined all the data from Steps 2,3 and 4 and store validation results in the validation columns of the manifest table.
Based on the final validation statuses, we return a message as it was described at the beginning of this project.


* Step 2 gives you data needed for NameValidation, DoBValidation, and BoardingPassValidation
* Step 3 gives you data needed for Person Identity Validation (PersonValidation)
* Step 4 gives you data needed for LuggageValidation

Based on the above-mentioned data, we performed the different validations:

* **Person Name Validation**: The first and last name extracted from the boarding pass and ID card must match with the name on the flight manifest table

* **DoB Validation**: DoB extracted from the ID card match with the flight manifest table

* **Boarding Pass Validation**: Various flight-specific information extracted from the boarding pass is matched with the flight manifest table. The information includes flight number, seat number, class, origin, destination, flight date, and flight time

* **Person Identity Validation**: Face extracted from the ID and that from the video should match, and the match result should be 65% or higher

* **Luggage Validation**: The carry-on loose items in the passenger's pocket contain a lighter in it or not.

Lastly, we update the flight manifest table with validation results. Set validation status value to TRUE for successful validation and to FALSE if validation failed.
For luggage validation, i used one image, since we don't have a way to match luggage validation with passengers.

Sample Passenger Manifest Table after the validation
Sample Passenger Manifest Table after the validation

After collected the informations from various sources, validate various pieces of information, we finally combined the validation results. Based on the validation results in the manifest table, we return a message.

