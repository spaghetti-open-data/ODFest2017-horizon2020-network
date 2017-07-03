# Powered by Python 2.7

# remove nodes with no stable partnerships
# run from the stable

from tulip import tlp

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
  stableDegree = graph.getDoubleProperty("stableDegree")
  viewLayout = graph.getLayoutProperty("viewLayout")
  viewMetric = graph.getDoubleProperty("viewMetric")
  KCore = graph.getDoubleProperty("K-Core")
  TentativeSIC = graph.getStringProperty("TentativeSIC")
  acronym = graph.getStringProperty("acronym")
  activityType = graph.getStringProperty("activityType")
  barPower = graph.getDoubleProperty("barPower")
  betwCentrality = graph.getDoubleProperty("betwCentrality")
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
  moneyTogether = graph.getDoubleProperty("moneyTogether")
  myMoney = graph.getDoubleProperty("myMoney")
  name = graph.getStringProperty("name")
  numPartners = graph.getDoubleProperty("numPartners")
  numProjects = graph.getDoubleProperty("numProjects")
  objective = graph.getStringProperty("objective")
  orgId = graph.getStringProperty("orgId")
  organizationUrl = graph.getStringProperty("organizationUrl")
  postCode = graph.getStringProperty("postCode")
  programme = graph.getStringProperty("programme")
  projectNode = graph.getBooleanProperty("projectNode")
  projectUrl = graph.getStringProperty("projectUrl")
  projectsTogether = graph.getIntegerProperty("projectsTogether")
  rcn = graph.getStringProperty("rcn")
  relationshipValue = graph.getDoubleProperty("relationshipValue")
  role = graph.getStringProperty("role")
  shortName = graph.getStringProperty("shortName")
  startDate = graph.getStringProperty("startDate")
  status = graph.getStringProperty("status")
  street = graph.getStringProperty("street")
  topics = graph.getStringProperty("topics")
  totMoney = graph.getDoubleProperty("totMoney")
  totalCost = graph.getDoubleProperty("totalCost")
  viewBorderColor = graph.getColorProperty("viewBorderColor")
  viewBorderWidth = graph.getDoubleProperty("viewBorderWidth")
  viewColor = graph.getColorProperty("viewColor")
  viewFont = graph.getStringProperty("viewFont")
  viewFontSize = graph.getIntegerProperty("viewFontSize")
  viewIcon = graph.getStringProperty("viewIcon")
  viewLabel = graph.getStringProperty("viewLabel")
  viewLabelBorderColor = graph.getColorProperty("viewLabelBorderColor")
  viewLabelBorderWidth = graph.getDoubleProperty("viewLabelBorderWidth")
  viewLabelColor = graph.getColorProperty("viewLabelColor")
  viewLabelPosition = graph.getIntegerProperty("viewLabelPosition")
  viewRotation = graph.getDoubleProperty("viewRotation")
  viewSelection = graph.getBooleanProperty("viewSelection")
  viewShape = graph.getIntegerProperty("viewShape")
  viewSize = graph.getSizeProperty("viewSize")
  viewSrcAnchorShape = graph.getIntegerProperty("viewSrcAnchorShape")
  viewSrcAnchorSize = graph.getSizeProperty("viewSrcAnchorSize")
  viewTexture = graph.getStringProperty("viewTexture")
  viewTgtAnchorShape = graph.getIntegerProperty("viewTgtAnchorShape")
  viewTgtAnchorSize = graph.getSizeProperty("viewTgtAnchorSize")
  wBarPower = graph.getDoubleProperty("wBarPower")
  weightedBarPower = graph.getDoubleProperty("weightedBarPower")
  
  stablePartners = graph.getDoubleProperty('stablePartners')  
  for n in graph.getNodes():
    stablePartners[n] = stableDegree[n] / 2 # there are two edges for each partners, one in and one out.
    if stableDegree[n] == 0:
      graph.delNode(n)


  
#    neighbors = []
#    for e in graph.getInOutEdges(n):
#      source = graph.source(e)
#      target = graph.target(e)
#      if source != n and source not in neighbors:
#        neighbors.append(source)
#      if target != n and target not in neighbors:
#        neighbors.append(target)
#    if len(neighbors) < 2:
#      toDelete.append(n)
#      
#    for node in toDelete:
#      graph.delNode(node)
# 
    
    
      
