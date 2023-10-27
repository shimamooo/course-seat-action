# Course Seat Availability Notifier

This repository hosts a set of Python scripts and a GitHub Actions workflow tailored to periodically monitor seat availability in various courses. In the event of an available seat, you will receive an email notification. The design is modular, ensuring ease of adding individualized logic for each course.

## Table of Contents
1. [Overview](#overview)
2. [How It Works](#how-it-works)
3. [Requirements](#requirements)
4. [Usage](#usage)
5. [Adding New Courses](#adding-new-courses)
6. [Credits](#credits)
7. [Screenshots](#screenshots)

## Overview

The `main.py` script at the heart of this repository meticulously checks the seat availability of specific courses, as listed in `COURSE_TO_DETECT`. The GitHub Actions workflow is configured to trigger upon any push to the `main` branch and can also be manually initiated. Following the initial trigger, it is set to run at 5-minute intervals. In circumstances where a seat becomes available in any of the listed courses, the workflow is deliberately designed to fail. This intentional failure serves as a trigger for GitHub to send you an email notification. To utilize this feature, ensure that your GitHub settings are configured to notify you in the event of workflow failures.

## How It Works

1. **Environment Setup**: The GitHub Actions workflow establishes a Python environment and proceeds to install all necessary dependencies.
2. **Seat Availability Check**: The `main.py` script is then executed to assess the seat availability for each course specified in `COURSE_TO_DETECT`. Each course is represented by its own Python script within the `courses` directory.
3. **Notification Trigger**: If an available seat is detected in any course, the script exits with a status code of 1. This exit code results in the failure of the GitHub Actions job, subsequently triggering a notification.
4. **No Availability**: In the absence of available seats, the script communicates the unavailability through a printed message and exits gracefully with a status code of 0, indicating successful execution of the process.

## Requirements

- Python 3.x
- Required Python packages (listed in `requirements.txt`)

## Usage

1. Clone the repository:
   ```
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name
   ```

2. (Optional) Add additional courses to the `COURSE_TO_DETECT` list in `main.py`.

3. Push your changes to the `main` branch to trigger the GitHub Actions workflow:
   ```
   git add .
   git commit -m "Add new courses"
   git push origin main
   ```

4. The GitHub Actions workflow will now run automatically every 5 minutes. You can also manually trigger it from the GitHub repository's Actions tab.

5. If a seat is available in any of the courses, the workflow will fail and you can receive an email notification. Make sure you have [configured GitHub to notify you on workflow failures](https://github.com/settings/notifications).
<img width="957" alt="image" src="https://github.com/perryzjc/course-seat-tracker-action/assets/92573736/7cd2f0b5-d6b4-48d5-a17c-737c4d50429b">


## Adding New Courses

To add a new course for tracking:

1. Create a new Python script in the `courses` directory, following the template of the existing course scripts.
2. Add the course's class name to the `COURSE_TO_DETECT` list in `main.py`.
3. Make sure the course script includes the logic to check seat availability and return the proper message.

## Credits 

**Authorship**:
- Jingchao Zhong [@perryzjc](https://github.com/perryzjc)

## Screenshots

1. **GitHub Actions Workflow**:
<img width="1715" alt="image" src="https://github.com/perryzjc/course-seat-tracker-action/assets/92573736/6a07f7e8-5be9-4022-9283-7d2caee81071">
<img width="1715" alt="image" src="https://github.com/perryzjc/course-seat-tracker-action/assets/92573736/351fc9d1-0082-463a-8360-3c220086b260">

2. **Notification Email**:
<img width="400" alt="image" src="https://github.com/perryzjc/course-seat-tracker-action/assets/92573736/da0d4987-1abb-49d9-b714-4a6ae8452cb8">

3. **Adding a New Course**: <img width="1715" alt="image" src="https://github.com/perryzjc/course-seat-tracker-action/assets/92573736/a8cb13c1-07f8-4a04-b384-1d8cb6d1c455">
