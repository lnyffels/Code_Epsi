# Created by S611372 at 05/11/2019
Feature: Department
  # Enter feature description here

  Scenario: CountNumber
    # Enter steps here
    Given I have 2 departments in a list MaList
    When I count each items
    Then I should have two in number