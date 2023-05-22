#!/usr/bin/env python3


class Person:
    # List of approved job titles
    approved_jobs = [
        "Admin",
        "Customer Service",
        "Human Resources",
        "ITC",
        "Production",
        "Legal",
        "Finance",
        "Sales",
        "General Management",
        "Research & Development",
        "Marketing",
        "Purchasing",
    ]

    def __init__(self, name=None, job=None):
        # Initialize private variables for name and job
        self._name = None
        self._job = None

        if name is not None:
            self.name = name
            # If a name is provided during initialization, set it using the property setter

        if job is not None:
            self.job = job
            # If a job is provided during initialization, set it using the property setter

    @property
    def name(self):
        return self._name
        # Getter method for the name property

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            if 1 <= len(value) <= 25:
                self._name = value.title()
                # If the value is a string between 1 and 25 characters, set the name
            else:
                print("Name must be a string between 1 and 25 characters.")
                # Print an error message if the name length is invalid
        else:
            print("Name must be a string between 1 and 25 characters.")
            # Print an error message if the name is not a string

    @property
    def job(self):
        return self._job
        # Getter method for the job property

    @job.setter
    def job(self, value):
        if value in self.approved_jobs:
            self._job = value
            # If the value is in the list of approved jobs, set the job
        else:
            print("Job must be in the list of approved jobs.")
            # Print an error message if the job is not in the approved jobs list
