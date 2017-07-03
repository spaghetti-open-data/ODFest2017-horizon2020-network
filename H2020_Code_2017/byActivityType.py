# Powered by Python 2.7

# To cancel the modifications performed by the script
# on the current graph, click on the undo button.

# Some useful keyboards shortcuts : 
#   * Ctrl + D : comment selected lines.
#   * Ctrl + Shift + D  : uncomment selected lines.
#   * Ctrl + I : indent selected lines.
#   * Ctrl + Shift + I  : unindent selected lines.
#   * Ctrl + Return  : run script.
#   * Ctrl + F  : find selected text.
#   * Ctrl + R  : replace selected text.
#   * Ctrl + Space  : show auto-completion dialog.

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
  KCore = graph.getDoubleProperty("K-Core")
  viewLayout = graph.getLayoutProperty("viewLayout")
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
  
  companies = 0
  companiesMoney = 0
  universities = 0
  universitiesMoney = 0
  researchCenters = 0
  resCenMoney = 0 
  publicSector = 0
  pubSecMoney = 0
  other = 0
  otherMoney = 0
  missing = 0
  missingMoney = 0

  for n in graph.getNodes():
    if activityType[n] == 'PRC':
      companies += 1
      companiesMoney += myMoney[n]
    elif activityType[n] == 'HES':
      universities += 1
      universitiesMoney += myMoney[n]
    elif activityType[n] == 'OTH':
      other += 1
      otherMoney += myMoney[n]
    elif activityType[n] == 'PUB':
      publicSector += 1
      pubSecMoney += myMoney[n]
    elif activityType[n] == 'REC':
      researchCenters += 1
      resCenMoney += myMoney[n]
    else:
      missing += 1
      missingMoney += myMoney[n]
      
  total = companies + universities + other + publicSector + researchCenters + missing
  totalMoney = companiesMoney + universitiesMoney + otherMoney + pubSecMoney + resCenMoney + missingMoney
  
  print ('PRC: ' + str(companies) + ' (' + str(companies/float(total)) + ')')
  print ('EUR ' + str(companiesMoney) + ' (' + str(float(companiesMoney)/totalMoney) + ')')
  print ('HES: ' + str(universities) + ' (' + str(universities/float(total)) + ')')
  print ('EUR ' + str(universitiesMoney) + ' (' + str(float(universitiesMoney)/totalMoney) + ')')
  print ('OTH: ' + str(other) + ' (' + str(other/float(total)) + ')')
  print ('EUR ' + str(otherMoney) + ' (' + str(float(otherMoney)/totalMoney) + ')')
  print ('PUB: ' + str(publicSector) + ' (' + str(float(publicSector)/total) + ')')
  print ('EUR ' + str(pubSecMoney) + ' (' + str(float(pubSecMoney)/totalMoney) + ')')
  print ('REC: ' + str(researchCenters) + ' (' + str(float(researchCenters)/total) + ')')
  print ('EUR ' + str(resCenMoney) + ' (' + str(float(resCenMoney)/totalMoney) + ')')
  print ('missing: ' + str(missing) + ' (' + str(float(missing)/total) + ')')
  print ('EUR ' + str(missingMoney) + ' (' + str(float(missingMoney)/totalMoney) + ')')
  

