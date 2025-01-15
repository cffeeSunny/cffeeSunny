from email.policy import default


def broad_firewall(
        packet: dict, filter_rules: list, default_policy: str
) -> str:

    if len(filter_rules) == 0:
        return default_policy
    if len(filter_rules) == 1:
        thing1 = filter_rules[0]
        criteria1 = thing1["attribute"]
        source_key1 = packet [criteria1]
        if thing1["action"] == "Allowlist":
            action = "Allow"
        elif thing1["action"] == "Blocklist":
            action = "Blocked"
        correct1 = source_key1 in thing1 ["values"]
        if correct1:
            return action
        else:
            return default_policy
    if len(filter_rules) == 2:
        thing1 = filter_rules[0]
        criteria1 = thing1["attribute"]
        source_key1 = packet[criteria1]
        action1 = thing1["action"]
        thing2 = filter_rules[1]
        criteria2 = thing2["attribute"]
        source_key2 = packet[criteria2]
        action2 = thing2["action"]
        correct1 = source_key1 in thing1["values"]
        correct2 = source_key2 in thing2["values"]
        if correct1 == False and action1 == "Blocked":
            action1 = "Allowed"
        if  correct2 == False and action2 == "Blocked":
            action2 = "Allowed"
        if action1 != action2:
            action = "Blocked"
        elif action1 == action2:
            action = action1[:5] + "ed"
        if correct1 and correct2 :
            return action
        else:
            return default_policy
    if len(filter_rules) == 3:
        thing1 = filter_rules[0]
        criteria1 = thing1["attribute"]
        source_key1 = packet[criteria1]
        action1 = thing1["action"]
        thing2 = filter_rules[1]
        criteria2 = thing2["attribute"]
        source_key2 = packet[criteria2]
        action2 = thing2["action"]
        thing3 = filter_rules[2]
        criteria3 = thing3["attribute"]
        source_key3 = packet[criteria3]
        action3 = thing3["action"]
        correct1 = source_key1 in thing1["values"]
        correct2 = source_key2 in thing2["values"]
        correct3 = source_key3 in thing3["values"]
        if  correct1 == False and action1 == "Blocked":
            action1 = "Allowed"
        if  correct2 == False and action2 == "Blocked":
            action2 = "Allowed"
        if  correct3 == False and action3 == "Blocked":
            action3 = "Allowed"

        if action1 == action2 == action3:
            action = action1[:5] + "ed"
        else:
            action = "Blocked"
        if correct1 and correct2 and correct3:
            return action
        else:
            return default_policy
    if len(filter_rules) == 4:
        thing1 = filter_rules[0]
        criteria1 = thing1["attribute"]
        source_key1 = packet[criteria1]
        action1 = thing1["action"]
        thing2 = filter_rules[1]
        criteria2 = thing2["attribute"]
        source_key2 = packet[criteria2]
        action2 = thing2["action"]
        thing3 = filter_rules[2]
        criteria3 = thing3["attribute"]
        source_key3 = packet[criteria3]
        action3 = thing3["action"]
        thing4 = filter_rules[3]
        criteria4 = thing4["attribute"]
        source_key4 = packet[criteria4]
        action4 = thing4["action"]
        correct1 = source_key1 in thing1["values"]
        correct2 = source_key2 in thing2["values"]
        correct3 = source_key3 in thing3["values"]
        correct4 = source_key4 in thing4["values"]

        if  correct1 == False and action1 == "Blocked":
            action1 = "Allowed"
        if  correct2 == False and action2 == "Blocked":
            action2 = "Allowed"
        if  correct3 == False and action3 == "Blocked":
            action3 = "Allowed"
        if  correct4 == False and action4 == "Blocked":
            action4 = "Allowed"

        action1n2 = action1 == action2
        action3n4 = action3 == action4
        if action1n2 == action3n4:
            action = action1[:5] + "ed"
        else:
            action = "Blocked"

        if correct1 and correct2 and correct3 and correct4:
            return action
        else:
            return default_policy
    if len(filter_rules) == 5:
        thing1 = filter_rules[0]
        criteria1 = thing1["attribute"]
        source_key1 = packet[criteria1]
        action1 = thing1["action"]
        thing2 = filter_rules[1]
        criteria2 = thing2["attribute"]
        source_key2 = packet[criteria2]
        action2 = thing2["action"]
        thing3 = filter_rules[2]
        criteria3 = thing3["attribute"]
        source_key3 = packet[criteria3]
        action3 = thing3["action"]
        thing4 = filter_rules[3]
        criteria4 = thing4["attribute"]
        source_key4 = packet[criteria4]
        action4 = thing4["action"]
        thing5 = filter_rules[4]
        criteria5 = thing5["attribute"]
        source_key5 = packet[criteria5]
        action5 = thing5["action"]
        correct1 = source_key1 in thing1["values"]
        correct2 = source_key2 in thing2["values"]
        correct3 = source_key3 in thing3["values"]
        correct4 = source_key4 in thing4["values"]
        correct5 = source_key5 in thing5["values"]
        if  correct1 == False and action1 == "Blocked":
            action1 = "Allowed"
        if  correct2 == False and action2 == "Blocked":
            action2 = "Allowed"
        if  correct3 == False and action3 == "Blocked":
            action3 = "Allowed"
        if  correct4 == False and action4 == "Blocked":
            action4 = "Allowed"
        if  correct5 == False and action5 == "Blocked":
            action5 = "Allowed"


        action1n2 = action1 == action2
        action3n4 = action3 == action4
        action3n4n5 = action3n4 == action5
        if action1n2 == action3n4n5:
            action = action1[:5] + "ed"
        else: action = "Blocked"

        correct1n2 = correct1 and correct2
        correct3n4 = correct3 and correct4
        if correct1n2 and correct3n4 and correct5:
            return action
        else:
            return default_policy
