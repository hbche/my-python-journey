from secret_agent_property import SecretAgent

mouse = SecretAgent("Mouse")
mouse.inform("Parmesano")
print(mouse.secret)         # None
mouse.secret = "12345 Main Street"
print(mouse.secret)         # ϗϘϙϚϛφϳЇЏДφϹКИЋЋК
mouse.secret = "555-1234"
print(mouse.secret)         # ϛϛϛϓϗϘϙϚ        

print(mouse._secrets)       # ['ϗϘϙϚϛφϳЇЏДφϹКИЋЋК', 'ϛϛϛϓϗϘϙϚ']
del mouse.secret
print(mouse._secrets)       # []