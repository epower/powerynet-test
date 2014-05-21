Feature: showing off www.powery.net

  Scenario: 
     Given I browse to www.powery.net
      when I look at the page for Archive
      then I should see Archive
