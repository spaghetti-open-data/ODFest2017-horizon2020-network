# Powered by Python 2.7

# exports weighted bargaining power as csv.
# run from stable

import csv
from tulip import tlp
dirPath = '/Users/albertocottica/github/local/ODFest2017-horizon2020-network/H2020_Data_2017/'

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
  rcn = graph.getStringProperty("rcn")
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
  wBarPower = graph.getDoubleProperty("wBarPower")
  weightedBarPower = graph.getDoubleProperty("weightedBarPower")
  stablePartners = graph.getDoubleProperty('stablePartners')
  
  gC = graph.getSubGraph('stableGC')
  
  # make a list and populated it with all nodes that are part of the giant component.
  inGC = []
  for nGC in gC.getNodes():
    inGC.append(nGC)

  # next, make another list and populate it with all nodes that are NOT in the first list.
  outGC = []
  for n in graph.getNodes():
    if n not in inGC:
      outGC.append(n)
      
  # make a list of dicts for export as csv. Dicts have the form [GC]n: weightedBarPower[n], where
  # [GC]n takes value 1 if the node is in the giant component, 0 otherwise.
  
  listOfDicts = []
  for nGC in inGC:
    row = {}
    row['weightedBarPower'] = weightedBarPower[nGC]
    row['numProjects'] = numProjects[nGC]
    row['stablePartners'] = stablePartners[nGC]
    row['GC'] = True
    row['activityType'] = activityType[nGC]
    row['betwCentrality'] = betwCentrality[nGC]
    listOfDicts.append(row)
    
  for n in outGC:
    row = {}
    row['weightedBarPower'] = weightedBarPower[n]
    row['numProjects'] = numProjects[n]
    row['stablePartners'] = stablePartners[n]
    row['GC'] = False
    row['activityType'] = activityType[n]
    row['betwCentrality'] = betwCentrality[n]
    listOfDicts.append(row)
    
  with open(dirPath + 'weightedBarPowerByComp.csv', 'w') as outFile:
    fieldnames = ['GC', 'weightedBarPower', 'numProjects', 'stablePartners', 'activityType', 'betwCentrality']
    writer = csv.DictWriter(outFile, fieldnames = fieldnames)
    success = writer.writeheader()
    for row in listOfDicts:
      success = writer.writerow(row)
