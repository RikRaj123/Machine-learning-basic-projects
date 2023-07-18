from plyer import notification  
  
notification_title = 'Hey this is Rik'  
notification_message = 'Thank you . Have a Good Day.'  
  
notification.notify(  
    title = notification_title,  
    message = notification_message,  
    app_icon = None,  
    timeout = 5,  
    toast = True  
    )  