#__________________NOTES______________________
# This is Finances version 0.3
# This update includes a login at the beginning
# and a welcome screen. It also is a streamlining
# of the GUI design and shorter code. The system
# will use text grabbing developed as part of
# Finances 0.2

#__________________IMPORTS____________________
import pygame
import time
import datetime

#__________________INITIALIZATIONS____________
pygame.init()

clock          = pygame.time.Clock()
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

DISPLAY_WIDTH = 1024
DISPLAY_HEIGHT = 768
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Finance Handler')

cover_x         = DISPLAY_WIDTH-299
cover_y         = DISPLAY_HEIGHT-59
cover_width     = 299
cover_height    = 29
height          = [60,90,120,150,180,210,240,270,300] # this is y in function ()


Finances_Exit   = False
Objectives_Show = False
Back            = False
Justin          = False
Jessica         = False


Justin_Checking           = 371.72
Justin_Bank_Savings       = 54.01
Jessica_Checking          = 1000
Jessica_Bank_Savings      = 2000

Current_Save_Rate_Justin  = 0
Cureent_Save_Rate_Jessica = 0

    #______________TEXT VARIABLES
number = 0
text = ''
typed_text = ''
Header_Text = 'Status: '
Status_Text = 'Current Bank Savings: %d' % Justin_Bank_Savings
Options_Text = 'Pay Stub Entry   Remove Savings  Adjust Rates   Add Obj  Bills'

Bills = {
    'Comcast':40.00,
    'PGE':30.00, 
    'T-Mobile':173.63,
    'Att Phone':50,
    'X-Box Live': 10.00,
    'OneDrive': 2.00,
    'Icloud': 2.00,
    'Google Play Music':15.00,
    'All State Car Insurance': 150,
    'Horace Mann Insurance_Car':81.45,
    'LinkedIn':30.00,
    'Wolfram':6.00,
    'Adobe Export PDF':24.00,
    'Rent':1695.00
    }
    

Jessica_Objectives = {
    'Travel': 0,
    'New Laptop':0,
    'Sewing Machine': 0,
    'Christmas': 0,
    'AppleWatch': 400,
    'Bike': 0
    }
    
Jessica_Objectives_success = {
    'Travel': 5000,
    'New Laptop':10000,
    'Sewing Machine': 2000,
    'Christmas': 2000,
    'AppleWatch': 400,
    'Bike': 400
    }

Justin_Objectives = {
    'Business_Seed': 0,
    'Denver':0,
    'Macbook': 0,
    'Surface2': 0,
    'AppleWatch': 400,
    'Bike': 0
    }
    
Justin_Objectives_success = {
    'Business_Seed': 5000,
    'Denver':10000,
    'Macbook': 2000,
    'Surface2': 2000,
    'AppleWatch': 400,
    'Bike': 400
    }

#__________________COLORS_____________________
Green = (26,255,128)
Amber = (255,182,66)
Blue  = (46,207,255)
White = (192,255,255)
Black = (0,0,0)
COLOR = White
#__________________FONTS______________________
FallFont  = pygame.font.Font('monofonto.ttf', 20)
SmallFall = pygame.font.Font('monofonto.ttf', 15)

#__________________FUNCTIONS__________________

def Login():
    Header_Text =   'Welcome to Finances. Please Sign in....'
    Status_Text =   'Enter Username to Continue'
    Options_Text =  ''
    main_display(Header_Text, Status_Text, Options_Text)
    entry_of_text()
    

def main_display(Header_Text, Status_Text, Options_Text):
    print('Main Display')
    gameDisplay.fill(Black)
    pygame.draw.line(gameDisplay, COLOR, (0, DISPLAY_HEIGHT - 30) , (DISPLAY_WIDTH, DISPLAY_HEIGHT - 30))
    pygame.draw.line(gameDisplay, COLOR, (0, 52) , (DISPLAY_WIDTH, 52))
    pygame.draw.line(gameDisplay, COLOR, (DISPLAY_WIDTH-300, DISPLAY_HEIGHT-60) , (DISPLAY_WIDTH, DISPLAY_HEIGHT-60))
    pygame.draw.line(gameDisplay, COLOR, (DISPLAY_WIDTH-300, DISPLAY_HEIGHT-30) , (DISPLAY_WIDTH-300, DISPLAY_HEIGHT-60))
    Headertext = FallFont.render('%s' % Header_Text,True, COLOR)
    Statustext = FallFont.render('%s' % Status_Text,True, COLOR)
    Optiontext = FallFont.render('%s' % Options_Text, True, COLOR)     
    
    gameDisplay.blit(Headertext,(0,0))
    gameDisplay.blit(Statustext,(0,30))
    gameDisplay.blit(Optiontext,(0,DISPLAY_HEIGHT-25))

    pygame.display.update()
    clock.tick(20)

def entry_of_number():
    Entry = False
    global number
    text = '0'
    while not Entry:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                new_text = pygame.key.name(event.key)
                text += new_text
                pygame.draw.rect(gameDisplay, Black, [cover_x,cover_y,cover_width, cover_height])
                text_objects(text, FallFont)
                display_text(text)

                if event.key == pygame.K_RETURN:
                    Entry =  True
                    Finances_Exit = True
                    global COLOR
                    pygame.draw.rect(gameDisplay, Black, [cover_x,cover_y,cover_width, cover_height])
                    pygame.display.update()
                    typed_text = text
                    number = int(typed_text)
                    print (typed_text)
                    return number
                else:
                    new_text = pygame.key.name(event.key)
                    if new_text == 'right shift' or new_text == 'left shift':
                        new_text = ''
                    if new_text == 'space':
                        new_text = ' '
                    if new_text == 'backspace':
                        new_text = ''
                        text = text[:-1]
                    if new_text == 'left':
                        new_text = ''
                        COLOR = Green
                        return COLOR
                    if new_text == 'right':
                        new_text = ''
                        COLOR = Blue
                        return COLOR
                    if new_text == 'up':
                        new_text = ''
                        COLOR = Amber
                        return COLOR
                    if new_text == 'down':
                        new_text = ''
                        COLOR = White
                        return COLOR
                    if new_text == 'return':
                        new_text = ''
                    text += new_text
                    pygame.draw.rect(gameDisplay, Black, [cover_x,cover_y,cover_width, cover_height])
                    text_objects(text, FallFont)
                    display_text(text)

def entry_of_text():
    print('etering text')
    Entry = False
    text = ''
    while not Entry:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                while pygame.key.get_mods() and pygame.KMOD_SHIFT:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            new_text = pygame.key.name(event.key)
                            new_text = new_text.upper()
                            text += new_text
                            pygame.draw.rect(gameDisplay, Black, [cover_x,cover_y,cover_width, cover_height])
                            text_objects(text, FallFont)
                            display_text(text)
                
                if event.key == pygame.K_RETURN:
                    Entry =  True
                    Finances_Exit = True
                    global COLOR
                    pygame.draw.rect(gameDisplay, Black, [cover_x,cover_y,cover_width, cover_height])
                    pygame.display.update()
                    typed_text = text
                    print (typed_text)
                    #--------LOGIN_-----------
                    if typed_text == 'ATLAS':
                        global Justin
                        Justin = True
                        return Justin
                    if typed_text == 'JESSICA':
                        global Jessica
                        Jessica = True
                        return Jessica
                    #--------Primary-----------
                    if typed_text == 'Pay Stub Entry':
                        Pay_Stub_Entry()
                    if typed_text == 'Savings':
                        Remove_Savings()
                    if typed_text == 'Adjust Rates':
                        Adjust_Rates()
                    if typed_text == 'Add Obj':
                        Add_Objective()
                    if typed_text == 'Bills':
                        Bill_Analysis(height[0])
                    #----------Back and Close--
                    if typed_text == 'Back' or typed_text == 'BACK':
                        Back           = True
                        Finances_Exit  = False
                        global Objectives_Show
                        Objectives_Show = False
                        Finances_Loop(height[0])
                    if typed_text == 'Close' or typed_text == 'CLOSE':
                        pygame.quit()
                        quit()
                    #---------Secondary-------
                    if typed_text == 'Entry':
                        PayStub_Handling()
                    if typed_text == 'Remove':
                        Remove_Savings_True()
                    if typed_text == 'Choose Rate':
                        Rate_Change()
                    if typed_text == 'Add':
                        Add_Objective_True(height[0])
                    if typed_text == 'Edit':
                        Bill_Edit(height[0])
                    else:
                        text = 'INVALID'
                        text_objects(text, FallFont)
                        display_text(text)
        
                
                else:
                    new_text = pygame.key.name(event.key)
                    if new_text == 'right shift' or new_text == 'left shift':
                        new_text = ''
                    if new_text == 'space':
                        new_text = ' '
                    if new_text == 'backspace':
                        new_text = ''
                        text = text[:-1]
                    if new_text == 'left':
                        new_text = ''
                        COLOR = Green
                        return COLOR
                    if new_text == 'right':
                        new_text = ''
                        COLOR = Blue
                        return COLOR
                    if new_text == 'up':
                        new_text = ''
                        COLOR = Amber
                        return COLOR
                    if new_text == 'down':
                        new_text = ''
                        COLOR = White
                        return COLOR
                    text += new_text
                    pygame.draw.rect(gameDisplay, Black, [cover_x,cover_y,cover_width, cover_height])
                    text_objects(text, FallFont)
                    display_text(text)
    
def text_objects(text, font):
    textSurface = font.render(text, True, COLOR)
    return textSurface, textSurface.get_rect()

def display_text(text):
    TextSurf, TextRect = text_objects(text, FallFont)
    TextRect.center = ((DISPLAY_WIDTH-150),(DISPLAY_HEIGHT-45))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def TextShift():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_mods() and pygame.KMOD_SHIFT:
                new_text = pygame.key.name(event.key)
                new_text = new_text.upper()
                text += new_text
                pygame.draw.rect(gameDisplay, Black, [cover_x,cover_y,cover_width, cover_height])
                text_objects(text, FallFont)
                display_text(text)

def objectives_show(y):
    global Objectives_Show
    global height
    y_start_point = y
    if Justin == True:
        for objective, amount_saved in Justin_Objectives.items():
            Middle_Text = objective
            middletext = FallFont.render('%s' % Middle_Text, True, COLOR)
            Side_Text = amount_saved
            sidetext = FallFont.render('%s' % Side_Text, True, COLOR)
            Success_Text = Justin_Objectives_success[objective]
            successtext = FallFont.render('%s' % Success_Text, True, COLOR)
            bar_start = FallFont.render('>|', True, COLOR)
            bar_end = FallFont.render('|<', True, COLOR)
            gameDisplay.blit(middletext,(0,y_start_point))
            gameDisplay.blit(sidetext,(300,y_start_point))
            gameDisplay.blit(bar_start,(380, y_start_point))
            gameDisplay.blit(bar_end,(800, y_start_point))
            gameDisplay.blit(successtext, (900,y_start_point))
            pygame.draw.rect(gameDisplay, COLOR, [400,y_start_point+7,(Side_Text/Success_Text)*400 , 16])
            y_start_point += 20
            pygame.display.update()
            Objectives_Show = True
    if Jessica == True:
        for objective, amount_saved in Jessica_Objectives.items():
            Middle_Text = objective
            middletext = FallFont.render('%s' % Middle_Text, True, COLOR)
            Side_Text = amount_saved
            sidetext = FallFont.render('%s' % Side_Text, True, COLOR)
            Success_Text = Jessica_Objectives_success[objective]
            successtext = FallFont.render('%s' % Success_Text, True, COLOR)
            bar_start = FallFont.render('>|', True, COLOR)
            bar_end = FallFont.render('|<', True, COLOR)
            gameDisplay.blit(middletext,(0,y_start_point))
            gameDisplay.blit(sidetext,(300,y_start_point))
            gameDisplay.blit(bar_start,(380, y_start_point))
            gameDisplay.blit(bar_end,(800, y_start_point))
            gameDisplay.blit(successtext, (900,y_start_point))
            pygame.draw.rect(gameDisplay, COLOR, [400,y_start_point+7,(Side_Text/Success_Text)*400 , 16])
            y_start_point += 20
            pygame.display.update()
            Objectives_Show = True
    
#__________________First Level________________   
def Pay_Stub_Entry():
    Back = False
    Header_Text =  'Enter a Paystub'
    Status_Text =  'Current Bank Savings: %d' % Justin_Bank_Savings
    Options_Text = 'BACK<<   >>Entry'
    print (Header_Text)
    main_display(Header_Text, Status_Text, Options_Text)
    while not Back:
        entry_of_text()

def Remove_Savings():
    print('Remove Savings')
    Back = False
    Header_Text =   'Remove Savings'
    Status_Text =   'Current Bank Savings: %d, Below is a log of your savings removal.' % Justin_Bank_Savings
    Options_Text =  'BACK<<   >>Remove'
    main_display(Header_Text, Status_Text, Options_Text)
    while not Back:
        entry_of_text()

def Adjust_Rates():
    print('Adjust Rate')
    Back = False
    Header_Text =   'Adjust Rates'
    Status_Text =   'Current Bank Savings: %d' % Justin_Bank_Savings
    Options_Text =  'BACK<<   >>Choose Rate'
    main_display(Header_Text, Status_Text, Options_Text)
    while not Back:
        entry_of_text()

def Add_Objective():
    print('Add Objective')
    Back = False
    Header_Text =   'Add an Objective '
    Status_Text =   'Current Bank Savings: %d' % Justin_Bank_Savings
    Options_Text =  'BACK<<   >>Add'
    main_display(Header_Text, Status_Text, Options_Text)
    while not Back:
        entry_of_text()

                    
def Bill_Analysis(y):
    
    y_start_point = y
    Back = False
    Bill_Show = False
    Total = 0
    Header_Text =  'Current Bills'
    Status_Text =  'Current Bank Savings: %d' % Justin_Bank_Savings
    Options_Text = 'BACK<<   >>Edit'
    main_display(Header_Text, Status_Text, Options_Text)
    while not Bill_Show:
        for bills, amount in Bills.items():
            Middle_Text = bills
            middletext = FallFont.render('%s' % Middle_Text, True, COLOR)
            Side_Text = amount
            sidetext = FallFont.render('%s' % Side_Text, True, COLOR)
            gameDisplay.blit(middletext,(0,y_start_point))
            gameDisplay.blit(sidetext,(300,y_start_point))
            Total += amount
            y_start_point += 20
            pygame.display.update()
        BillsTotal_Text = 'Total: '
        BillsTotal_Amount = str(Total)
        billstotaltext = FallFont.render('%s' % BillsTotal_Text, True, COLOR)
        billstotalamount = FallFont.render('%s' % BillsTotal_Amount, True, COLOR) 
        gameDisplay.blit(billstotaltext,(0,y_start_point+20))
        gameDisplay.blit(billstotalamount,(300,y_start_point+20))
        pygame.display.update()
        Bill_Show = True
        while not Back:
            entry_of_text()

#__________________Second Level_______________

def PayStub_Handling():
    print('PayStub_Handling')
    global Justin
    global Jessica
    Back = False
    welcome = ''
    if Justin == True:
        welcome = 'Justin'
    if Jessica == True:
        welcome = 'Jessica'
    Header_Text =  'Hello %s looks like you are making money!' % welcome
    Status_Text =  ''
    Options_Text = 'B - BACK<<'
    main_display(Header_Text, Status_Text, Options_Text)
    entry_of_text()
    while not Back:
        entry_of_text()

def Remove_Savings_True():
    global Justin
    global Jessica
    global Justin_Bank_Savings
    global Jessica_Bank_Savings
    global number
    Back = False
    savings_show = 0
    if Justin == True:
        savings_show = Justin_Bank_Savings
    if Jessica == True:
        savings_show = Jessica_Bank_Savings
    Header_Text =  'Your Current Savings are %d' % savings_show
    Status_Text =  'Enter the amount to be removed'
    Options_Text = 'B - BACK<<'
    main_display(Header_Text, Status_Text, Options_Text)
    while not Back:        
        entry_of_number()
    Back = False
    if Justin ==  True:
        Justin_Bank_Savings-=number
    if Jessica == True:
        Jessica_Bank_Savings -= number
    while not Back:
        entry_of_text()

def Rate_Change():
    global Justin
    global Jessica
    Back = False
    rate_show = 0
    if Justin == True:
        rate_show = Current_Save_Rate_Justin
    if Jessica == True:
        rate_show = Current_Save_Rate_Jessica
    Header_Text =  'Your Current Savings Rate is %d' % rate_show
    Status_Text =  'Caution: You risk longterm goals. Consider entering "No Change"'
    Options_Text = 'B - BACK<<'
    main_display(Header_Text, Status_Text, Options_Text)
    while not Back:
        entry_of_text()

def Add_Objective_True(y):
    global Justin
    global Jessica

    y_start_point = y
    global Objectives_Show
    Objectives_Show = False
    Back = False
    Header_Text =  'Adding Objectives Stretches Focus'
    Status_Text =  'Note: secret goals require entry of "Secret"'
    Options_Text = 'B - BACK<<'
    main_display(Header_Text, Status_Text, Options_Text)
    while not Objectives_Show:
        objectives_show(height[0])
    while not Back:
        entry_of_text()
        
def Bill_Edit(y):
    print('You are editing bills...')
    Back = False
    Bill_Show = False
    
    y_start_point = y
    Total = 0
    Header_Text =  'Bill Editing'
    Status_Text =  'Enter the Name of the bill you wish to edit as it appears'
    Options_Text = 'B - BACK<<'
    main_display(Header_Text, Status_Text, Options_Text)
    while not Bill_Show:
        for bills, amount in Bills.items():
               Middle_Text = bills
               middletext = FallFont.render('%s' % Middle_Text, True, COLOR)
               Side_Text = amount
               sidetext = FallFont.render('%s' % Side_Text, True, COLOR)
               gameDisplay.blit(middletext,(0,y_start_point))
               gameDisplay.blit(sidetext,(300,y_start_point))
               Total += amount
               y_start_point += 20
               pygame.display.update()
        BillsTotal_Text = 'Total: '
        BillsTotal_Amount = str(Total)
        billstotaltext = FallFont.render('%s' % BillsTotal_Text, True, COLOR)
        billstotalamount = FallFont.render('%s' % BillsTotal_Amount, True, COLOR) 
        gameDisplay.blit(billstotaltext,(0,y_start_point +20))
        gameDisplay.blit(billstotalamount,(300,y_start_point +20))
        pygame.display.update()
        Bill_Show = True
    while not Back:
        entry_of_text()

#__________________Third Level________________


#__________________DEF LOOP___________________
def Finances_Loop(y):
    global Justin
    global Jessica
    
    global Objectives_Show
    y_start_point = y

    welcome = ''
    if Justin == True:
        welcome = 'Justin'
    if Jessica == True:
        welcome = 'Jessica'
    print('Finances Loop')
    print(Justin)
    print (y_start_point)
    
    Header_Text =  'Hello %s here is a snapshot of your financials' % welcome
    Status_Text =  'Today is %s' % st
    Options_Text = '-Pay Stub Entry  -Savings  -Adjust Rates   -Add Obj  -Bills'
    main_display(Header_Text, Status_Text, Options_Text)
    while not Objectives_Show:
        Line_Text = 'Currently your savings are: $%d' % Justin_Bank_Savings
        Linetext = FallFont.render('%s' % Line_Text, True, COLOR)
        gameDisplay.blit(Linetext,(0,y_start_point))
        pygame.display.update()
        y_start_point += 20
        Line_Text = 'You are saving from your pay at a rate of %d percent.' % Current_Save_Rate_Justin
        Linetext = FallFont.render('%s' % Line_Text, True, COLOR)
        gameDisplay.blit(Linetext,(0,y_start_point))
        y_start_point += 30
        Line_Text = 'Your monthly bills amount to: %d' % Current_Save_Rate_Justin
        Linetext = FallFont.render('%s' % Line_Text, True, COLOR)
        gameDisplay.blit(Linetext,(0,y_start_point))
        y_start_point += 30
        Line_Text = 'Here are your current goals and progress:'
        Linetext = FallFont.render('%s' % Line_Text, True, COLOR)
        gameDisplay.blit(Linetext,(0,y_start_point))
        y_start_point += 20
        pygame.display.update()
        
        objectives_show(height[5])
    while not Finances_Exit:
        entry_of_text()


#__________________LOOP_______________________        
Login()
Finances_Loop(height[0])
pygame.quit()
quit()


