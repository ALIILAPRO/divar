import telebot

bot = telebot.TeleBot('YOUR_BOT_TOKEN')

@bot.message_handler(commands=['restart'])
def handle_restart(message):
	# Code to execute when the /restart command is received
	# This code will restart the "shadowbox" Docker container

	# Execute the "docker restart shadowbox" command
	import subprocess
	try:
		subprocess.check_output(['docker', 'restart', 'shadowbox'])
		bot.send_message(message.chat.id, "Docker container restarted successfully.")
	except subprocess.CalledProcessError as e:
		bot.send_message(message.chat.id, f"Error restarting Docker container:\n{e.output}")

bot.polling()