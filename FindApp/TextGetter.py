
class TextGetter:

	"""
	class TextGetter for storing and getting different text
	"""
	
	def __init__(self):
	
		"""
		add texts types here and create getter methods e.g. textAbout and get_textAbout
		"""
		
		self.textAbout=[
            "Добропожаловать в FindApp!",
            "Выполнили:\n\n Илья Седунов \n и Вадим Альперович,\n\n 17ПМИ\n2019",
           "Дисклеймер:\n Осторожно, важная информация!!!",
            """В наше время люди все чаще и чаще\n пытаются деморализировать ситуацию в стране,\n
            хотя есть инфа...""",
            """И в целях дестабилизации ситуации в стране пятой колоной 
            было придумано оружие массового поражения российских граждан 
            называемое ...""",
            """...МИТИНГ...""",
            """Но, к счастью, команда(двое) опытных разработчиков создала панцею \n
               от данных проблем общества - приложение FindApp©""",
            """Приложение FindApp© поможет зафиксировать и отследить всех школьников \n
               посещавших и посещающих митиги \n
               для контроля и дальнейшего принятия соотвествующих мер(ремень)...""",
            'Так к делу!\n\n\n\n ...\n Authors: Sedunov & Alperovich \n 17PMI'
          ]
	def get_textAbout(self):
	
		"""
		@return textAbout a main "about" storytelling
		"""
		
		return self.textAbout