from django.db import models as m

class User(m.Model):
    user_id = m.BigIntegerField(primary_key=True) # Primary key: Google-defined User ID
    codename = m.CharField(max_length=32) # Ingress codename
    first_visit = m.DateTimeField(auto_now_add=True) # Date this record was created
    latest_visit = m.DateTimeField() # Date of user's most recent use of the site
    prefs = m.CharField(max_length=1024) # Perhaps a pickled preferences object could be stored here?
    user_comment = m.TextField(max_length=1024) # Comment by the user themselves, i.e. "about me".
    access_level = m.IntegerField() # Quartermaster access level

class UserComment(m.Model):
    key = m.IntegerField(primary_key=True) # ID
    timestamp = m.DateTimeField(auto_now_add=True) # Date submitted
    location = m.BigIntegerField(primary_key=True) # Whose profile is it submitted on
    submitter = m.BigIntegerField(primary_key=True) # Who submitted it
    content = m.TextField() # Contents

class AgentInventory(m.Model):
    "Represents an agent's inventory."
    agent_id = m.BigIntegerField(primary_key=True) # ID of the user whose inventory this is
    action_points = m.IntegerField() # Action Points of this agent
    item_count = m.IntegerField() # Cached item count
    last_update = m.DateTimeField(auto_now=True, auto_now_add=True) # Date of last update
    portal_keys = m.IntegerField() # Number of portal keys
    resonators = m.CommaSeparatedIntegerField(max_length=32) # Number of resonators (by level)
    bursters = m.CommaSeparatedIntegerField(max_length=32) # Number of bursters (by level)
    power_cubes = m.CommaSeparatedIntegerField(max_length=32) # Number of Power Cubes (by level)
    shields = m.CommaSeparatedIntegerField(max_length=16) # Number of shields (by rarity)
    heatsinks = m.CommaSeparatedIntegerField(max_length=16) # Number of Heatsinks (by rarity)
    multi_hacks = m.CommaSeparatedIntegerField(max_length=16) # Number of Multi-Hacks (by rarity)
    force_amps = m.CommaSeparatedIntegerField(max_length=16) # Number of Force Amps (by rarity)
    turrets = m.CommaSeparatedIntegerField(max_length=16) # Number of Turrets (by rarity)
    link_amps = m.CommaSeparatedIntegerField(max_length=16) # Number of Link Amps (by rarity)
    viruses = m.CommaSeparatedIntegerField(max_length=8) # Number of Viruses (by rarity)
    other = m.IntegerField() # Number of other items (i.e. media)
