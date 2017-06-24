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

import datetime
from tulip import *

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
  barPower = graph.getDoubleProperty("barPower")
  viewLayout = graph.getLayoutProperty("viewLayout")
  wBarPower = graph.getDoubleProperty("wBarPower")
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

  bipartite = graph.getSubGraph('bipartite_no_EA')
  orgs2orgs = graph.addSubGraph('orgs2orgs')
  
  # add nodes first
  for p in bipartite.getNodes():
	  	if projectNode.getNodeValue(p) == False:
	  		orgs2orgs.addNode(p)
  
  for p in bipartite.getNodes(): # iterate over nodes...
		if projectNode.getNodeValue(p) == True: # only for project-type nodes
			projectAcronym = acronym.getNodeValue(p)
			participants = []
			for e in bipartite.getInEdges(p):
			  	participants.append(bipartite.source(e))
			for e in bipartite.getInEdges(p):
			  	thisPartnershipValue = ecContribution.getEdgeValue(e)
			  	edgeSource = bipartite.source(e)
			  	for participant in participants:
			  		if participant != edgeSource:
			  			newEdge = orgs2orgs.addEdge(edgeSource, participant)
			  			acronym[newEdge] = acronym[p]
			  			call[newEdge] = call[p]
			  			totalCost[newEdge] = totalCost[p]
			  			ecMaxContribution[newEdge] = ecMaxContribution[p]
			  			ecContribution[newEdge] = thisPartnershipValue
			  			programme[newEdge] = programme[p]
			  			startDate[newEdge] = startDate[p]
			  			endDate[newEdge] = endDate[p]
			  			topics[newEdge] = topics[p]
							
  end_script = datetime.datetime.now()
  
  print ('Runtime: ' + str (end_script - start_script))

					
