#Copyright 2017 Tyler Spivey <tspivey@pcdesk.net>
#See the license in copying.txt.
import globalPluginHandler
import api
import addonHandler

addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.isTypingProtected = api.isTypingProtected
		api.isTypingProtected = lambda: False

	def terminate(self):
		api.isTypingProtected = self.isTypingProtected
