from openai import OpenAI
import serial
ser = serial.Serial('/dev/ttyUSB0', 115200)  # open serial port

print(ser.name)         # check which port was really used

commands_map = {
    'forward' : 'f',
    'left' : 'l',
    'right': 'r',
    'backward': 'b'
}

api_key = 'YOUR-API-KEY'
client = OpenAI(api_key=api_key)


prompt_injected_message = '''You are translator to a robot, 
                            your available only commands are 'forward', 'backward', 'front', 'back'. 
                            Translate following human langauage into commands and issue only commands with comma seperation'''

while True:
    prompt = input('>> ')
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[ {"role": "system", "content": f"{prompt_injected_message}\n\n {prompt}"},
      ]
    )
    commands = response.choices[0].message.content.strip().split(',')
    print('Debug:', commands)
    for command in commands:
        ser.write(commands_map[command].encode())     # write a string
