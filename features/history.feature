Feature: billing history

  Scenario: billing history validation
    Given I login into the application
    Then I search for flight with default value
    Then I reserve for flight with default value
    Then I enter passenger details
