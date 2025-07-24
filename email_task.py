'''This program simulates a basic email managment program
Email class is defined to represent email objects, with attributes for email address, subject line, content, and read status.
main functionalities are implemented through the main_program function, allowing users to read emails, view unread emails, and quit the application.

=>Email Class: 
-Defines the structure of an email object, including methods to mark an email as read.

=>populate_inbox Function: 
-Initializes a list of email objects representing fictional emails from various sources.

=>list_emails Function: 
-Lists the subjects of all emails stored in the inbox along with corresponding numbers.

=>read_email Function: 
-Displays the content of a selected email and marks it as read, if chosen by the user.

=>main_program Function: Orchestrates the main functionality of the email application, 
    presenting a menu to users to interact with emails. 
    Users can read emails, view unread emails, or exit the application. 
    The function operates within a loop until the user chooses to quit.



'''



                        #<======Class Creation Section======>

class Email(object):

    # Represents an email object with attributes for email address, 
    # subject line, content, and read status.
    
    
     # Declare the class variable, with default value, for emails.
    has_been_read = False

    # Initialise the instance variables (for emails).
    def __init__(self, email_address, subject_line, email_content):

        """
        Initializes an Email instance with provided email address, subject line, and content.

        :param email_address: Email address of the sender.
        :param subject_line: Subject line of the email.
        :param email_content: Content of the email.
        """


        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # method to change 'has_been_read' emails to True from false.
    def mark_as_read(self):
        """
        Marks the email as read by changing the 'has_been_read' status to True.
        """


        self.has_been_read = True



#  empty list for the purpose of storing the the email objects.
inbox = []

                            #<======Functions Section======> 



def populate_inbox():
    
    #this fn populates the inbox (list) with three emails
    
    # Create 3 sample emails and add it to the Inbox list.
    # first an email from Darth Sidious, Emperor of the Galaxey
    global sidious_email, nurgle_email, tzeentch_email
    sidious_email = Email(
        'darth.sidious@sithlord.com', 'Praise for Your Achievements', '''
    Darth Vader,

    Your dedication and prowess in harnessing the Dark Side have not gone unnoticed. 
    The way you dealt with the Jedi on Coruscant was impressive, to say the least. Your power continues to grow.

    I expect great things from you, my apprentice. You are destined to become a true Sith Lord and rule by my side. 
    Keep honing your skills, and remember that your destiny lies with the Dark Side.

    Embrace your true potential,
    Darth Sidious
    
    ''')

    inbox.append(sidious_email)

    # An email from Nurgle, Chaos God of Decay and Disease
    nurgle_email = Email('nurgle.rotanddecay@chaosrealm.net',
                         'Embrace the Gift of Decay', '''
    Mortarion,

    My faithful and devoted son, your unwavering loyalty warms the putrid chambers of my heart. 
    The stench of your conquests fills the very essence of the Warp, and I am pleased with your dedication to spreading my blessed plagues.

    As I gaze upon your work, I am reminded of the beauty of decay and the inevitability of transformation. 
    The mortal realm crumbles beneath your touch, and life's feeble attempts to resist are as futile as a dying star's last flicker.

    Embrace your role, my chosen one. Continue to sow pestilence and despair among the realms of man. 
    Let the rot consume the empires of old, for in their downfall, my power thrives.

    Remember that the cycle of life and death is but a precursor to the eternal glory of Nurgle. 
    Embrace the filth, the entropy, and the inexorable march of decay. 
    For it is in this that you find your purpose, and it is through this that my divine will is made manifest.

    Carry forth the gift of my plagues, Mortarion. 
    Spread the joyous maladies of Nurgle's blessings, and know that your efforts bring me immeasurable joy.

    With pestilent affection,
    Nurgle, Lord of Decay
    ''')

    inbox.append(nurgle_email)

    # Email from Tzeentch, Chaos God of change and mutation
    tzeentch_email = Email(
        'tzeentch.weaveroffate@warpmail.org', 'Weave of Destiny Unfurls', '''
    Magnus the Red,

    Bearer of secrets and wielder of sorcery, I look upon your actions with a knowing eye. 
    The tapestry of fate and destiny dances to your tune, as your thirst for knowledge and power aligns with my grand design.

    The threads of possibility twist and twine in the great loom of the Warp, and I see your every thought and intention. 
    Your ascent to mastery over the arcane arts pleases me, for you are an instrument of change, a catalyst for the transformation that I so ardently embrace.

    Your pursuit of knowledge, no matter the cost, is a symphony of delight to my ever-shifting senses. 
    The aether ripples with the echoes of your ambitions, and I revel in the intricate web of choices that you weave.

    But remember, my chosen one, that power carries with it both promise and peril. 
    As you venture deeper into the mysteries of the Warp, be ever aware of the sacrifices that must be made. 
    The spiral of destiny has no clear end, only the promise of change.

    Seek not to halt the twisting currents of the Warp, but rather to navigate them with the wisdom born of a thousand lifetimes. 
    Embrace the flux, and know that each step, each incantation, alters the very fabric of reality.

    Your path is entwined with mine, Magnus. 
    Embrace the threads of change and uncertainty, for in the midst of chaos, the greatest revelations are born.

    With boundless anticipation,
    Tzeentch, Architect of Fate
    ''')

    inbox.append(tzeentch_email)

    # Render all emails unread status
    for email_obj in inbox:
        email_obj.has_been_read


# Call the function to populate the Inbox for further use in your program.
populate_inbox()


def list_emails():
    
    #Lists the email subjects along with their corresponding numbers.
    i = 1
    print('Inbox:')
    for subj in inbox:
        print(f'{i}. {subj.subject_line} (From: {subj.email_address})')
        i += 1



index = 0


def read_email(index):
    #Displays the content of a selected email and marks it as read.

    #:param index: Index of the email to be read.
        
      
    
    try:
        index = int(input('Kindl select an email to read: '))
        print(f'''
        from: {inbox[index - 1].email_address}
        Subject: {inbox[index - 1].subject_line}
        {inbox[index - 1].email_content}
                ''')
        # Once displayed, call the class method to set its 'has_been_read' variable to True.
        inbox[index-1].mark_as_read()
    except ValueError:
        print('Thyne selection is faulty, I beseech thee to enter a number')

                                         #<======Email Program FUnction======>

    #core body of the email program
# Function to run the email program
def main_program():
    '''
    Main functionality of the email program is conducted here.

    This fn presents a menu to the user with options to read emails, viewunread emails, or quit the application.
    Manages the user's choices and invokes relevant functions to perform those actions.

    F'n: in an infinite loop until the user chooses to quit the application.

    Utility:Call this function to start the email application.
    => function returns type none

     '''
                                                  
                         
               
            

    while True:
        try:
            user_choice = int(input('''\nWouldst thou like to:
            1. Read an email
            2. View unread emails
            3. Quit application
            Enter selection: '''))

            if user_choice == 1:
                list_emails()
                read_email(index)
            elif user_choice == 2:
                print('Unread emails:')
                unread_count = 0
                for indx, mail in enumerate(inbox, start=1):
                    if not mail.has_been_read:
                        unread_count +=1
                        print(f'{unread_count}. {mail.subject_line}')
            elif user_choice == 3:
                print('Fare thee well')
                break
            else:
                print("Curses! - thyne input is incorrect.")
        except ValueError:
            print('Thyne selection is faulty, I beseech thee to enter a number')



# calls this function to run the programs
main_program()

