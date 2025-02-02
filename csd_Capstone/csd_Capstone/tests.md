# Functional Test Cases for Authentication System

## Landing Page Tests

### Test 1: Landing Page Content and Navigation Verification

**Test Objective:** Verify all required elements are present and functional on the landing page
**Developer:** [Developer Name]
**Date tested:** [yyyy/mm/dd]
**Peer tester:** [Tester Name]
**Date tested:** [yyyy/mm/dd]

| Step | Action                           | Expected Results                                            | Developer pass/fail | Tester pass/fail | Screenshot   |
| ---- | -------------------------------- | ----------------------------------------------------------- | ------------------- | ---------------- | ------------ |
| 1    | Navigate to the landing page URL | Page loads with "Welcome to our Site" heading               | yes/no              | yes/no           | [Screenshot] |
| 2    | Check navigation menu items      | "Login" and "Register" links are visible when not logged in | yes/no              | yes/no           | [Screenshot] |
| 3    | Verify welcome message           | "Your secure authentication solution" text is displayed     | yes/no              | yes/no           | [Screenshot] |
| 4    | Check responsive design          | Page layout adjusts properly on mobile view (375px width)   | yes/no              | yes/no           | [Screenshot] |
| 5    | Verify navigation functionality  | Clicking "Login" navigates to login page                    | yes/no              | yes/no           | [Screenshot] |

**Comments:**
The landing page implementation provides clear navigation and responsive design. The content is well-organized and the user interface elements are properly positioned. Consider adding more engaging content or features for returning users.

### Test 2: Landing Page Authentication State

**Test Objective:** Verify landing page behavior changes based on authentication state
**Developer:** [Developer Name]
**Date tested:** [yyyy/mm/dd]
**Peer tester:** [Tester Name]
**Date tested:** [yyyy/mm/dd]

| Step | Action                        | Expected Results                                                     | Developer pass/fail | Tester pass/fail | Screenshot   |
| ---- | ----------------------------- | -------------------------------------------------------------------- | ------------------- | ---------------- | ------------ |
| 1    | Log in with valid credentials | User is redirected to landing page with authenticated state          | yes/no              | yes/no           | [Screenshot] |
| 2    | Check navigation menu         | "Logout" option and username are displayed instead of Login/Register | yes/no              | yes/no           | [Screenshot] |
| 3    | Verify welcome message        | Welcome message shows logged-in state                                | yes/no              | yes/no           | [Screenshot] |
| 4    | Click logout                  | User is logged out and returned to landing page                      | yes/no              | yes/no           | [Screenshot] |
| 5    | Verify state reset            | Login/Register buttons reappear                                      | yes/no              | yes/no           | [Screenshot] |

**Comments:**
The authentication state management works effectively. The UI updates appropriately based on user login status. The logout process is smooth and returns users to the correct state.

## Login Page Tests

### Test 3: Login Form Validation

**Test Objective:** Verify login form validation and error handling
**Developer:** [Developer Name]
**Date tested:** [yyyy/mm/dd]
**Peer tester:** [Tester Name]
**Date tested:** [yyyy/mm/dd]

| Step | Action                              | Expected Results                              | Developer pass/fail | Tester pass/fail | Screenshot   |
| ---- | ----------------------------------- | --------------------------------------------- | ------------------- | ---------------- | ------------ |
| 1    | Submit empty login form             | Form shows required field errors              | yes/no              | yes/no           | [Screenshot] |
| 2    | Enter invalid username format       | Form displays username error message          | yes/no              | yes/no           | [Screenshot] |
| 3    | Enter invalid password format       | Form displays password error message          | yes/no              | yes/no           | [Screenshot] |
| 4    | Enter non-existent user credentials | Shows "Invalid username or password" message  | yes/no              | yes/no           | [Screenshot] |
| 5    | Verify password field masking       | Password characters are hidden with asterisks | yes/no              | yes/no           | [Screenshot] |

**Comments:**
The login form validation provides appropriate feedback for all error cases. The error messages are clear and helpful. Consider adding password visibility toggle and remember me functionality.

### Test 4: Login Success Path

**Test Objective:** Verify successful login process and redirection
**Developer:** [Developer Name]
**Date tested:** [yyyy/mm/dd]
**Peer tester:** [Tester Name]
**Date tested:** [yyyy/mm/dd]

| Step | Action                            | Expected Results                                      | Developer pass/fail | Tester pass/fail | Screenshot   |
| ---- | --------------------------------- | ----------------------------------------------------- | ------------------- | ---------------- | ------------ |
| 1    | Enter valid username and password | Fields accept input properly                          | yes/no              | yes/no           | [Screenshot] |
| 2    | Submit login form                 | Form submits successfully                             | yes/no              | yes/no           | [Screenshot] |
| 3    | Verify redirect                   | User is redirected to landing page                    | yes/no              | yes/no           | [Screenshot] |
| 4    | Check success message             | "Login successful!" message appears                   | yes/no              | yes/no           | [Screenshot] |
| 5    | Verify session                    | User remains logged in when navigating to other pages | yes/no              | yes/no           | [Screenshot] |

**Comments:**
The login success path works smoothly with appropriate feedback and session handling. The redirect flow is intuitive and maintains proper state management.

## Registration Page Tests

### Test 5: Registration Form Validation

**Test Objective:** Verify registration form validation and error handling
**Developer:** Robert Stewart
**Date tested:** 1/31/2025
**Peer tester:** Robert Stewart
**Date tested:** 1/31/2025

| Step | Action                          | Expected Results                       | Developer pass/fail | Tester pass/fail | Screenshot   |
| ---- | ------------------------------- | -------------------------------------- | ------------------- | ---------------- | ------------ |
| 1    | Submit empty registration form  | Form shows required field errors       | yes/no              | yes/no           | [Screenshot] |
| 2    | Enter password that's too short | Shows minimum length requirement error | yes/no              | yes/no           | [Screenshot] |
| 3    | Enter mismatched passwords      | Shows password mismatch error          | yes/no              | yes/no           | [Screenshot] |
| 4    | Enter existing username         | Shows username already exists error    | yes/no              | yes/no           | [Screenshot] |
| 5    | Enter valid common password     | Shows password complexity error        | yes/no              | yes/no           | [Screenshot] |

**Comments:**
The registration form provides comprehensive validation with clear error messages. The password requirements are properly enforced. Consider adding a password strength indicator.

### Test 6: Registration Success Path

**Test Objective:** Verify successful registration process and account creation
**Developer:** [Developer Name]
**Date tested:** [yyyy/mm/dd]
**Peer tester:** [Tester Name]
**Date tested:** [yyyy/mm/dd]

| Step | Action                           | Expected Results                       | Developer pass/fail | Tester pass/fail | Screenshot   |
| ---- | -------------------------------- | -------------------------------------- | ------------------- | ---------------- | ------------ |
| 1    | Enter valid registration details | Form accepts all inputs                | yes/no              | yes/no           | [Screenshot] |
| 2    | Submit registration form         | Form submits successfully              | yes/no              | yes/no           | [Screenshot] |
| 3    | Verify account creation          | User account is created in database    | yes/no              | yes/no           | [Screenshot] |
| 4    | Check automatic login            | User is automatically logged in        | yes/no              | yes/no           | [Screenshot] |
| 5    | Verify welcome message           | Success message and username displayed | yes/no              | yes/no           | [Screenshot] |

**Comments:**
The registration process works efficiently with proper account creation and automatic login. The success flow provides good user feedback. Consider adding email verification for additional security.
