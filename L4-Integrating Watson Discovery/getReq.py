#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('bash', '', 'mkdir lab4\ncd lab4\ngit clone https://github.com/sophiajwchoi/Lab4-Adding-Discovery-to-Chatbot.git')


# In[1]:


get_ipython().run_cell_magic('bash', '', 'cd /resources/lab4/Lab4-Adding-Discovery-to-Chatbot\nexport npm_config_loglevel=silent\nconda config --set notify_outdated_conda false\nconda install nodejs -y\nrm -f ~/.npmrc\nnpm install')


# In[ ]:





# In[2]:


get_ipython().run_cell_magic('bash', '', 'ibmcloud config --check-version=false\nibmcloud login --no-region\nsubhamnitap@gmail.com\n@Biggboss1')


# In[4]:


get_ipython().run_cell_magic('bash', '', 'ibmcloud account orgs')


# In[7]:


get_ipython().run_cell_magic('bash', '', "ibmcloud target --cf-api 'https://api.eu-gb.cf.cloud.ibm.com' -r eu-gb -o subhamnitap@gmail.com\n# ibmcloud account space-create 'lab4'")


# In[8]:


get_ipython().run_cell_magic('bash', '', 'cd /resources/lab4/Lab4-Adding-Discovery-to-Chatbot\nibmcloud target -s lab4\nibmcloud plugin install cloud-functions -f\nexport npm_config_loglevel=silent\nnpm install -g serverless@1.51.0\nibmcloud fn --apihost eu-gb.functions.cloud.ibm.com\nibmcloud fn list --apihost eu-gb.functions.cloud.ibm.com\nserverless deploy')


# In[9]:


get_ipython().system('ibmcloud fn list')


# In[ ]:




