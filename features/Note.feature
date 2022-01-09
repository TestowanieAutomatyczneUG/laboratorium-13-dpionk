Feature: Note

	klasa zapisuje dane notatki, jeśli są dobrego typu.

	Scenario: name none
    When trying to create a note with none as a name
    Then the note won't be created

  Scenario: name empty
    When trying to create a note with an empty string as name
    Then the note won't be created

  Scenario: name not being a string
    When trying to create a note with a different datatype than string as name
    Then the note won't be created

  Scenario: name string
    When trying to create a note with a non empty string as name
    Then Note will be created

  Scenario: note float
    When trying to create a note with a different datatype than float as note
    Then the note won't be created

  Scenario: note less than 2
    When trying to create a note with a value less than 2 as note
    Then the note won't be created

  Scenario: note more than 6
    When trying to create a note with a value more than 6 as note
    Then the note won't be created

  Scenario: note between 2 and 6
    When trying to create a note with a value more than 2 and less than 6 as note
    Then Note will be created