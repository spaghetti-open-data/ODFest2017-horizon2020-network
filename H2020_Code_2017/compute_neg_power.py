# Run from the bipartite

import datetime
from tulip import *

# start the clock
start_script = datetime.datetime.now()

# The updateVisualization(centerViews = True) function can be called
# during script execution to update the opened views

# The pauseScript() function can be called to pause the script execution.
# To resume the script execution, you will have to click on the "Run script " button.

# The runGraphScript(scriptFile, graph) function can be called to launch
# another edited script on a tlp.Graph object.
# The scriptFile parameter defines the script name to call (in the form [a-zA-Z0-9_]+.py)

# The main(graph) function must be defined 
# to run the script on the current graph

def main(graph): 
  TentativeSIC = graph.getStringProperty("TentativeSIC")
  acronym = graph.getStringProperty("acronym")
  activityType = graph.getStringProperty("activityType")
  birthDate = graph.getIntegerProperty("birthDate")
  call = graph.getStringProperty("call")
  city = graph.getStringProperty("city")
  commDate = graph.getDoubleProperty("commDate")
  country = graph.getStringProperty("country")
  ecContribution = graph.getDoubleProperty("ecContribution")
  ecMaxContribution = graph.getDoubleProperty("ecMaxContribution")
  endDate = graph.getStringProperty("endDate")
  endOfParticipation = graph.getBooleanProperty("endOfParticipation")
  fundingScheme = graph.getStringProperty("fundingScheme")
  intimacy = graph.getDoubleProperty("intimacy")
  manager = graph.getBooleanProperty("manager")
  myMoney = graph.getDoubleProperty("myMoney")
  name = graph.getStringProperty("name")
  numPartners = graph.getIntegerProperty("numPartners")
  numProjects = graph.getIntegerProperty("numProjects")
  objective = graph.getStringProperty("objective")
  orgId = graph.getStringProperty("orgId")
  organizationUrl = graph.getStringProperty("organizationUrl")
  postCode = graph.getStringProperty("postCode")
  programme = graph.getStringProperty("programme")
  projectNode = graph.getBooleanProperty("projectNode")
  projectUrl = graph.getStringProperty("projectUrl")
  rcn = graph.getStringProperty("rcn")
  role = graph.getStringProperty("role")
  shortName = graph.getStringProperty("shortName")
  startDate = graph.getStringProperty("startDate")
  status = graph.getStringProperty("status")
  street = graph.getStringProperty("street")
  topics = graph.getStringProperty("topics")
  totalCost = graph.getDoubleProperty("totalCost")
  viewBorderColor = graph.getColorProperty("viewBorderColor")
  viewBorderWidth = graph.getDoubleProperty("viewBorderWidth")
  viewColor = graph.getColorProperty("viewColor")
  viewFont = graph.getStringProperty("viewFont")
  viewFontAwesomeIcon = graph.getStringProperty("viewFontAwesomeIcon")
  viewFontSize = graph.getIntegerProperty("viewFontSize")
  viewIcon = graph.getStringProperty("viewIcon")
  viewLabel = graph.getStringProperty("viewLabel")
  viewLabelBorderColor = graph.getColorProperty("viewLabelBorderColor")
  viewLabelBorderWidth = graph.getDoubleProperty("viewLabelBorderWidth")
  viewLabelColor = graph.getColorProperty("viewLabelColor")
  viewLabelPosition = graph.getIntegerProperty("viewLabelPosition")
  viewLayout = graph.getLayoutProperty("viewLayout")
  viewMetric = graph.getDoubleProperty("viewMetric")
  viewRotation = graph.getDoubleProperty("viewRotation")
  viewSelection = graph.getBooleanProperty("viewSelection")
  viewShape = graph.getIntegerProperty("viewShape")
  viewSize = graph.getSizeProperty("viewSize")
  viewSrcAnchorShape = graph.getIntegerProperty("viewSrcAnchorShape")
  viewSrcAnchorSize = graph.getSizeProperty("viewSrcAnchorSize")
  viewTexture = graph.getStringProperty("viewTexture")
  viewTgtAnchorShape = graph.getIntegerProperty("viewTgtAnchorShape")
  viewTgtAnchorSize = graph.getSizeProperty("viewTgtAnchorSize")
  
  # define a new property. The cut of the budget you get is a proxy of bargaining power
  barPower = graph.getDoubleProperty('barPower')
  # definition of barganing power af agent i across a project with budget B and N partners
  # barPower(i) = ( N * B(i) - B) / (N * B)
  # properties.
  # When the budget is equally distributed, barPower(i) = 0 because N * B(i) = B
  # When i takes more than 1/nth of B, barPower(i) is positive
  # When i takes less than 1/nth of B, barPower(i) is negative.
  # barPower is limited between -1 and +1. The -1 case corresponds to i taking nothing across infinite partners.
  # The + 1 case corresponds to i taking all of B across an infinite number of partners
  # The - 1 case corresponds to taking nothing of a project with infinite budget
  # the sum of barPowers across a project is always 0 (less rounding)
  # to sum barPower coefficients across different projects, I weight them by the budget. High-B projects weigh more.
  # suppose two projects j and k with budgets Bj and Bk.
  # barpower(i, w) = (barPower(i, j) * Bj + barPower(i, k) * Bk) / (Bj + Bk)
  
  # from the bipartite, compute bargaining Powers for each project. This is as edge property. 
  
  counter = 0
  for n in graph.getNodes():
    if projectNode[n] == True:
      counter += 1 
      budget = ecMaxContribution.getNodeValue(n)
      participants = []
      for e in graph.getInEdges(n):
        participants.append(graph.source(e))
      bigN = len(participants)
      for e in graph.getInEdges(n):
        barPower[e] = (bigN * ecContribution[e] - budget) / (bigN * budget)
        ecMaxContribution[e] = budget # I will need this later
  print (str(counter) + ' projects processed.')
      
  end_script = datetime.datetime.now()
  
  print ('Runtime: ' + str (end_script - start_script))
