# OrangeHRM Buzz Module Automation Testing Documentation

**Project:** Software Testing Automation – OrangeHRM Demo  
**Tester:** Gio Carlo S. Belda  
**Date:** 2025-12-16  
**Tools & Environment:**  
- **Browser:** Google Chrome 143.x  
- **Framework:** Selenium WebDriver (Python) + Pytest  
- **IDE:** PyCharm 2025  
- **OS:** Windows 11  
- **Test Data:** Random posts, photos from `C:\Users\U\Downloads`  

---

## 1. Project Planning & Test Design (15 pts)

| Criteria | Description | Implementation / Notes | Points |
|----------|-------------|----------------------|--------|
| Test Plan Quality | Clear scope, objectives, tools, environment, assumptions, constraints | Automate Buzz module features: login, posting, editing, deleting posts, media upload, UI verification. | 5 |
| Test Case Design | Well-structured test cases with steps, expected results, and prioritization | Test cases include login, navigation, post creation/editing/deletion, media upload, help icon, and filters. Assertions ensure correctness. | 5 |
| Choice of Scenarios | Relevant, realistic, automatable scenarios | Scenarios cover realistic user interactions in Buzz module: posting, editing with media, deleting, filtering posts, verifying UI elements. | 5 |

---

## 2. Selenium WebDriver Automation Implementation (30 pts)

| Criteria | Description | Implementation / Notes | Points |
|----------|-------------|----------------------|--------|
| Correct WebDriver Usage | Proper initialization, locators, waits, teardown | `webdriver.Chrome()` with fixture setup/teardown. `WebDriverWait` for dynamic elements. Locators mainly XPath with explicit waits. | 10 |
| Stability & Reliability | Handles dynamic elements, retry loops | Retry loops for stale elements, explicit waits ensure stable execution, handles dynamic post and UI updates. | 10 |
| Best Practices | POM usage, reusable functions, modular code | LoginPage uses Page Object Model. Tests are modular: separate functions for login, posting, editing, deleting, media uploads, and filters. | 10 |

---

## 3. Pytest Framework Implementation (20 pts)

| Criteria | Description | Implementation / Notes | Points |
|----------|-------------|----------------------|--------|
| Use of Fixtures | Setup/teardown implemented via fixtures | `driver()` fixture initializes Chrome browser, maximizes, navigates to login page, and quits after tests. | 7 |
| Pytest Structure & Organization | Test naming, assertions, conventions | All tests prefixed with `test_`. Assertions validate URL, toast messages, and UI element presence. | 7 |
| Test Execution & Parametrization | Pytest features | Tests can be run selectively. Parametrization can be added for multiple post contents or media files. | 6 |

---

## 4. Assertions, Reporting & Logging (15 pts)

| Criteria | Description | Implementation / Notes | Points |
|----------|-------------|----------------------|--------|
| Correct Assertions | Meaningful and complete | Assertions validate login success, post creation/editing, Buzz textarea visibility, toast messages, clickable icons/buttons. | 5 |
| Reporting Tools | Reporting and screenshots | Print statements log progress. `pytest-html` plugin can generate HTML reports. Screenshots can be added on failure for visual confirmation. | 5 |
| Logging & Error Handling | Readable logs, exception handling | Try/except blocks handle stale elements and confirmation dialogs. Print statements used for step progress. | 5 |

---

## 5. Code Quality & Documentation (10 pts)

| Criteria | Description | Implementation / Notes | Points |
|----------|-------------|----------------------|--------|
| Coding Standards | Readability, indentation, PEP8 | Well-indented code, descriptive variable names, comments included, follows PEP8 conventions. | 5 |
| Project Documentation | README or documentation | This Markdown file documents test cases, setup, environment, execution steps, and scenarios. | 5 |

---

## 6. Final Output, Presentation & Demo (10 pts)

| Criteria | Description | Implementation / Notes | Points |
|----------|-------------|----------------------|--------|
| Execution Demo | Live test execution | Tests executed successfully in PyCharm, console output confirms step completion. | 5 |
| Presentation Quality | Clarity in explaining design choices and results | Documentation explains test coverage, dynamic handling, modularity, and expected outcomes clearly. | 5 |

---

## 7. Test Cases Overview

| Test Case | Description | Key Assertions | Notes |
|-----------|------------|----------------|-------|
| `test_valid_login` | Login as Admin | Dashboard page loaded, URL contains 'dashboard' | Uses LoginPage POM |
| `test_click_buzz_menu` | Navigate to Buzz | Buzz textarea is displayed | Waits for clickable menu |
| `test_buzz_post` | Create a post | Success toast appears | Includes login in test itself |
| `test_click_edit_post` | Open edit post modal | Edit post option clickable | Verified modal interaction |
| `test_edit_post` | Edit first post with random photo | Photo attached, post text updated, post button clicked | Handles dynamic file upload |
| `test_delete_post` | Delete first post | Post deleted successfully | Handles confirmation dialogs |
| `test_click_most_liked_posts` | Filter by most liked | Button clicked successfully | Feed refresh wait included |
| `test_click_most_commented_posts` | Filter by most commented | Button clicked successfully | Feed refresh wait included |
| `test_click_share_photos_in_buzz` | Click Share Photos button | Button clicked successfully | Retry loop for stale elements |
| `test_click_share_video_in_buzz` | Click Share Video button | Button clicked successfully | Retry loop for dynamic DOM |
| `test_help_icon` | Verify help icon | Icon is clickable | UI element presence |
| `test_click_post_option` | Open post options (three dots) | Options menu clickable | Verified inside first post container |

---

**Notes:**  
- Screenshots can be added for each step for visual reporting.  
- `pytest-html` can generate detailed HTML reports for presentation/demo.  
- Parametrization can enhance coverage for multiple posts or media files.  
- Retry logic and explicit waits improve test reliability on dynamic elements.

---

✅ **This documentation is ready to be included in PyCharm as `Buzz_Automation_Test_Documentation.md`.**
