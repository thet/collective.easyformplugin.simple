# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s collective.easyformplugin.simple -t test_simple_form.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src collective.easyformplugin.simple.testing.ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/collective/easyformplugin/simple/tests/robot/test_simple_form.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Simple Form
  Given a logged-in site administrator
    and an add Simple Form form
   When I type 'My Simple Form' into the title field
    and I submit the form
   Then a Simple Form with the title 'My Simple Form' has been created

Scenario: As a site administrator I can view a Simple Form
  Given a logged-in site administrator
    and a Simple Form 'My Simple Form'
   When I go to the Simple Form view
   Then I can see the Simple Form title 'My Simple Form'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Simple Form form
  Go To  ${PLONE_URL}/++add++Simple Form

a Simple Form 'My Simple Form'
  Create content  type=Simple Form  id=my-simple_form  title=My Simple Form

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Simple Form view
  Go To  ${PLONE_URL}/my-simple_form
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Simple Form with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Simple Form title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
