import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="TestCraft AI",
    page_icon="🧪",
    layout="wide"
)


def add_test_case(
    test_cases,
    scenario,
    steps,
    expected_result,
    test_type,
    priority,
    risk_level,
    automation_candidate,
    recommended_tool,
    why_it_matters
):
    test_cases.append({
        "Scenario": scenario,
        "Steps": steps,
        "Expected Result": expected_result,
        "Type": test_type,
        "Priority": priority,
        "Risk Level": risk_level,
        "Automation Candidate": automation_candidate,
        "Recommended Tool": recommended_tool,
        "Why This Test Matters": why_it_matters
    })


def generate_test_cases(requirement):
    requirement_lower = requirement.lower()
    test_cases = []

    add_test_case(
        test_cases,
        "Verify the main successful user flow",
        "Enter valid data and complete the requested action.",
        "The system should complete the action successfully without errors.",
        "Positive",
        "High",
        "High",
        "Yes",
        "Selenium / Playwright",
        "This confirms that the core business flow works correctly for a valid user."
    )

    add_test_case(
        test_cases,
        "Verify required field validation",
        "Leave mandatory fields empty and submit the form.",
        "The system should display clear validation messages for required fields.",
        "Negative",
        "High",
        "Medium",
        "Yes",
        "Selenium / Playwright",
        "Required field validation prevents incomplete or incorrect data from entering the system."
    )

    add_test_case(
        test_cases,
        "Verify invalid input handling",
        "Enter invalid data and submit the form.",
        "The system should reject invalid input and display a proper error message.",
        "Negative",
        "Medium",
        "Medium",
        "Yes",
        "Selenium / Playwright",
        "Invalid input testing ensures the application handles user mistakes safely."
    )

    add_test_case(
        test_cases,
        "Verify special character and script input handling",
        "Enter special characters such as <script>alert('test')</script> and submit.",
        "The system should sanitize input and prevent script execution.",
        "Security",
        "High",
        "High",
        "Yes",
        "Selenium / Playwright / OWASP ZAP",
        "This helps identify possible cross-site scripting and input sanitization issues."
    )

    if "login" in requirement_lower or "sign in" in requirement_lower:
        add_test_case(
            test_cases,
            "Verify login with valid credentials",
            "Enter valid username/email and password, then click Login.",
            "User should be logged in and redirected to the dashboard.",
            "Positive",
            "High",
            "High",
            "Yes",
            "Selenium / Playwright",
            "Login is usually a critical entry point, so it must work reliably."
        )

        add_test_case(
            test_cases,
            "Verify login with invalid credentials",
            "Enter invalid username or password, then click Login.",
            "System should reject the login attempt and show an error message.",
            "Negative",
            "High",
            "High",
            "Yes",
            "Selenium / Playwright",
            "This ensures unauthorized users cannot access the system."
        )

        add_test_case(
            test_cases,
            "Verify account lockout after multiple failed login attempts",
            "Enter wrong credentials multiple times.",
            "System should lock the account or show a security warning based on business rules.",
            "Security",
            "High",
            "High",
            "Yes",
            "Selenium / Playwright",
            "This protects user accounts from brute-force login attempts."
        )

    if "password" in requirement_lower:
        add_test_case(
            test_cases,
            "Verify weak password validation",
            "Enter a weak password such as 12345 and submit.",
            "System should display a password strength validation message.",
            "Validation",
            "High",
            "High",
            "Yes",
            "Selenium / Playwright",
            "Password validation protects users from creating weak credentials."
        )

        add_test_case(
            test_cases,
            "Verify expired password reset link",
            "Open an expired password reset link.",
            "System should display a link expired message and prevent reset.",
            "Edge",
            "Medium",
            "High",
            "Yes",
            "Selenium / Playwright",
            "Expired links should not be reusable because that can create a security risk."
        )

        add_test_case(
            test_cases,
            "Verify password reset confirmation",
            "Complete password reset with valid details.",
            "System should confirm that the password was reset successfully.",
            "Positive",
            "High",
            "High",
            "Yes",
            "Selenium / Playwright",
            "This confirms that users can recover account access successfully."
        )

    if "email" in requirement_lower:
        add_test_case(
            test_cases,
            "Verify invalid email format",
            "Enter an invalid email format such as user@email and submit.",
            "System should display an invalid email format message.",
            "Validation",
            "High",
            "Medium",
            "Yes",
            "Selenium / Playwright",
            "Email validation prevents incorrect or unusable email addresses from being submitted."
        )

        add_test_case(
            test_cases,
            "Verify unregistered email handling",
            "Enter an email address that is not registered in the system.",
            "System should display an appropriate message without exposing account details.",
            "Negative",
            "High",
            "High",
            "Yes",
            "Selenium / Playwright",
            "This helps prevent account enumeration and protects user privacy."
        )

    if "payment" in requirement_lower or "card" in requirement_lower or "checkout" in requirement_lower:
        add_test_case(
            test_cases,
            "Verify successful payment with valid card details",
            "Enter valid card details and complete payment.",
            "Payment should be processed successfully and confirmation should be displayed.",
            "Positive",
            "High",
            "High",
            "Yes",
            "Selenium / Playwright / Postman",
            "Payment flows are business critical and directly affect revenue."
        )

        add_test_case(
            test_cases,
            "Verify declined payment handling",
            "Enter a declined or invalid card and submit payment.",
            "System should reject the payment and show a clear failure message.",
            "Negative",
            "High",
            "High",
            "Yes",
            "Selenium / Playwright / Postman",
            "Users should receive clear feedback when payment fails."
        )

        add_test_case(
            test_cases,
            "Verify payment without required billing information",
            "Leave billing details empty and attempt payment.",
            "System should prevent payment and show required field validation.",
            "Negative",
            "High",
            "High",
            "Yes",
            "Selenium / Playwright",
            "Billing validation prevents incomplete payment processing."
        )

    if "upload" in requirement_lower or "file" in requirement_lower:
        add_test_case(
            test_cases,
            "Verify valid file upload",
            "Upload a supported file type within the allowed file size.",
            "File should upload successfully and be available to the user.",
            "Positive",
            "High",
            "Medium",
            "Yes",
            "Selenium / Playwright",
            "File upload must work correctly because users rely on it to submit documents."
        )

        add_test_case(
            test_cases,
            "Verify unsupported file type upload",
            "Upload an unsupported file type such as .exe.",
            "System should reject the file and show a clear validation message.",
            "Negative",
            "High",
            "High",
            "Yes",
            "Selenium / Playwright",
            "This protects the system from unsafe or unsupported files."
        )

        add_test_case(
            test_cases,
            "Verify file size limit",
            "Upload a file larger than the allowed size.",
            "System should reject the file and display a file size limit message.",
            "Boundary",
            "Medium",
            "Medium",
            "Yes",
            "Selenium / Playwright",
            "File size validation prevents storage and performance issues."
        )

    if "search" in requirement_lower:
        add_test_case(
            test_cases,
            "Verify search with valid keyword",
            "Enter a valid keyword and click Search.",
            "Relevant search results should be displayed.",
            "Positive",
            "Medium",
            "Medium",
            "Yes",
            "Selenium / Playwright",
            "Search functionality helps users find information quickly."
        )

        add_test_case(
            test_cases,
            "Verify search with no matching results",
            "Enter a keyword that does not match any record.",
            "System should display a no results found message.",
            "Negative",
            "Medium",
            "Low",
            "Yes",
            "Selenium / Playwright",
            "This ensures users receive meaningful feedback when no data is found."
        )

    if "profile" in requirement_lower or "account" in requirement_lower:
        add_test_case(
            test_cases,
            "Verify profile update with valid details",
            "Update profile fields with valid information and save.",
            "Profile should be updated successfully.",
            "Positive",
            "Medium",
            "Medium",
            "Yes",
            "Selenium / Playwright",
            "Profile updates are important because users need control over their account details."
        )

        add_test_case(
            test_cases,
            "Verify profile update with invalid data",
            "Enter invalid profile data and save.",
            "System should display validation messages and prevent update.",
            "Negative",
            "Medium",
            "Medium",
            "Yes",
            "Selenium / Playwright",
            "This prevents bad data from being saved in user profiles."
        )

    if "api" in requirement_lower:
        add_test_case(
            test_cases,
            "Verify API response for valid request",
            "Send a valid API request with required parameters.",
            "API should return expected status code and response body.",
            "API",
            "High",
            "High",
            "Yes",
            "Postman / Pytest Requests",
            "API testing validates backend behavior independent of the user interface."
        )

        add_test_case(
            test_cases,
            "Verify API response for missing required parameter",
            "Send an API request without required parameters.",
            "API should return a proper error response.",
            "API Negative",
            "High",
            "High",
            "Yes",
            "Postman / Pytest Requests",
            "This confirms the API handles invalid requests correctly."
        )

    for index, test_case in enumerate(test_cases, start=1):
        test_case["Test Case ID"] = f"TC_{index:03d}"

    columns = [
        "Test Case ID",
        "Scenario",
        "Steps",
        "Expected Result",
        "Type",
        "Priority",
        "Risk Level",
        "Automation Candidate",
        "Recommended Tool",
        "Why This Test Matters"
    ]

    return pd.DataFrame(test_cases)[columns]


st.title("TestCraft AI")

st.write(
    "AI-assisted test case design, risk analysis, and automation planning from software requirements."
)

st.markdown("### Enter a user story or software requirement")

requirement = st.text_area(
    "Requirement",
    placeholder="Example: As a user, I want to reset my password using my registered email so that I can regain access to my account.",
    height=150
)

col1, col2, col3 = st.columns(3)

with col1:
    include_security = st.checkbox("Include security thinking", value=True)

with col2:
    include_automation = st.checkbox("Include automation recommendation", value=True)

with col3:
    include_reasoning = st.checkbox("Include QA reasoning", value=True)

if st.button("Generate TestCraft Test Cases"):
    if requirement.strip() == "":
        st.warning("Please enter a requirement or user story.")
    else:
        df = generate_test_cases(requirement)

        if not include_security:
            df = df[df["Type"] != "Security"]

        if not include_automation:
            df = df.drop(columns=["Automation Candidate", "Recommended Tool"])

        if not include_reasoning:
            df = df.drop(columns=["Why This Test Matters"])

        st.success("TestCraft AI generated the test cases successfully.")

        st.subheader("Generated Test Cases")
        st.dataframe(df, use_container_width=True)

        st.subheader("QA Summary")

        total_cases = len(df)
        high_priority = len(df[df["Priority"] == "High"]) if "Priority" in df.columns else 0
        high_risk = len(df[df["Risk Level"] == "High"]) if "Risk Level" in df.columns else 0

        summary_col1, summary_col2, summary_col3 = st.columns(3)

        summary_col1.metric("Total Test Cases", total_cases)
        summary_col2.metric("High Priority", high_priority)
        summary_col3.metric("High Risk", high_risk)

        st.subheader("Testing Strategy Notes")
        st.info(
            "Start automation with high-priority and high-risk test cases first. "
            "Positive flows, login, payment, password reset, and API tests are usually strong automation candidates."
        )

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download Test Cases as CSV",
            data=csv,
            file_name="testcraft_ai_test_cases.csv",
            mime="text/csv"
        )