#!/usr/bin/env python
# coding: utf-8

# In[15]:


from textblob import TextBlob


# In[16]:


from flask import Flask


# In[17]:


from flask import render_template, request


# In[18]:


app = Flask(__name__)


# In[19]:


@app.route("/", methods = ["GET", "POST"]) #before you run the function, to run this first -decorator
def index():
    if request.method == "POST":
        text = request.form.get("text")
        r = TextBlob(text).sentiment.polarity
        return(render_template("index.html", result=r))
    else:
        return(render_template("index.html", result="waiting...."))


# In[20]:


if __name__ == "__main__":
    app.run()


# In[ ]:


# 127.0.0.1 this is a reserved number to route to local, 5000 is a port, port is 0-9999. 

