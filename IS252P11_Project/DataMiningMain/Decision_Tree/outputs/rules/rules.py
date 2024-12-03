def findDecision(obj): #obj[0]: Gender, obj[1]: Customer Type, obj[2]: Age, obj[3]: Type of Travel, obj[4]: Class, obj[5]: Flight Distance, obj[6]: Inflight wifi service, obj[7]: Departure/Arrival time convenient, obj[8]: Ease of Online booking, obj[9]: Gate location, obj[10]: Food and drink, obj[11]: Online boarding, obj[12]: Seat comfort, obj[13]: Inflight entertainment, obj[14]: On-board service, obj[15]: Leg room service, obj[16]: Baggage handling, obj[17]: Checkin service, obj[18]: Inflight service, obj[19]: Cleanliness, obj[20]: Departure Delay in Minutes, obj[21]: Arrival Delay in Minutes
   # {"feature": "Online boarding", "instances": 25893, "metric_value": 0.9892, "depth": 1}
   if obj[11]>3:
      # {"feature": "Type of Travel", "instances": 12971, "metric_value": 0.8528, "depth": 2}
      if obj[3] == 'Business travel':
         # {"feature": "Inflight entertainment", "instances": 10319, "metric_value": 0.6035, "depth": 3}
         if obj[13]>3:
            # {"feature": "Customer Type", "instances": 7724, "metric_value": 0.368, "depth": 4}
            if obj[1] == 'Loyal Customer':
               # {"feature": "Inflight service", "instances": 7115, "metric_value": 0.2671, "depth": 5}
               if obj[18]<=4:
                  return 'satisfied'
               elif obj[18]>4:
                  return 'satisfied'
               else:
                  return 'satisfied'
            elif obj[1] == 'disloyal Customer':
               # {"feature": "Inflight wifi service", "instances": 609, "metric_value": 0.9451, "depth": 5}
               if obj[6]<=4:
                  return 'neutral or dissatisfied'
               elif obj[6]>4:
                  return 'satisfied'
               else:
                  return 'satisfied'
            else:
               return 'satisfied'
         elif obj[13]<=3:
            # {"feature": "Checkin service", "instances": 2595, "metric_value": 0.9555, "depth": 4}
            if obj[17]>2:
               # {"feature": "Inflight wifi service", "instances": 2071, "metric_value": 0.8365, "depth": 5}
               if obj[6]<=4:
                  return 'satisfied'
               elif obj[6]>4:
                  return 'satisfied'
               else:
                  return 'satisfied'
            elif obj[17]<=2:
               # {"feature": "Inflight wifi service", "instances": 524, "metric_value": 0.6992, "depth": 5}
               if obj[6]<=4:
                  return 'neutral or dissatisfied'
               elif obj[6]>4:
                  return 'satisfied'
               else:
                  return 'neutral or dissatisfied'
            else:
               return 'satisfied'
         else:
            return 'satisfied'
      elif obj[3] == 'Personal Travel':
         # {"feature": "Inflight wifi service", "instances": 2652, "metric_value": 0.7487, "depth": 3}
         if obj[6]<=4:
            # {"feature": "Ease of Online booking", "instances": 2372, "metric_value": 0.5322, "depth": 4}
            if obj[8]>3:
               # {"feature": "Arrival Delay in Minutes", "instances": 1245, "metric_value": 0.7362, "depth": 5}
               if obj[21]<=10.76144578313253:
                  return 'neutral or dissatisfied'
               elif obj[21]>10.76144578313253:
                  return 'neutral or dissatisfied'
               else:
                  return 'neutral or dissatisfied'
            elif obj[8]<=3:
               # {"feature": "Leg room service", "instances": 1127, "metric_value": 0.1725, "depth": 5}
               if obj[15]>0:
                  return 'neutral or dissatisfied'
               elif obj[15]<=0:
                  return 'neutral or dissatisfied'
               else:
                  return 'neutral or dissatisfied'
            else:
               return 'neutral or dissatisfied'
         elif obj[6]>4:
            return 'satisfied'
         else:
            return 'neutral or dissatisfied'
      else:
         return 'satisfied'
   elif obj[11]<=3:
      # {"feature": "Inflight wifi service", "instances": 12922, "metric_value": 0.6219, "depth": 2}
      if obj[6]>0:
         # {"feature": "Class", "instances": 12442, "metric_value": 0.5362, "depth": 3}
         if obj[4] == 'Eco':
            # {"feature": "Ease of Online booking", "instances": 7416, "metric_value": 0.2854, "depth": 4}
            if obj[8]<=3:
               # {"feature": "Type of Travel", "instances": 6791, "metric_value": 0.2099, "depth": 5}
               if obj[3] == 'Personal Travel':
                  return 'neutral or dissatisfied'
               elif obj[3] == 'Business travel':
                  return 'neutral or dissatisfied'
               else:
                  return 'neutral or dissatisfied'
            elif obj[8]>3:
               # {"feature": "Inflight entertainment", "instances": 625, "metric_value": 0.7787, "depth": 5}
               if obj[13]<=3:
                  return 'neutral or dissatisfied'
               elif obj[13]>3:
                  return 'satisfied'
               else:
                  return 'neutral or dissatisfied'
            else:
               return 'neutral or dissatisfied'
         elif obj[4] == 'Business':
            # {"feature": "Leg room service", "instances": 3851, "metric_value": 0.8536, "depth": 4}
            if obj[15]<=3:
               # {"feature": "Checkin service", "instances": 2021, "metric_value": 0.4546, "depth": 5}
               if obj[17]<=4:
                  return 'neutral or dissatisfied'
               elif obj[17]>4:
                  return 'neutral or dissatisfied'
               else:
                  return 'neutral or dissatisfied'
            elif obj[15]>3:
               # {"feature": "Customer Type", "instances": 1830, "metric_value": 0.9989, "depth": 5}
               if obj[1] == 'Loyal Customer':
                  return 'satisfied'
               elif obj[1] == 'disloyal Customer':
                  return 'neutral or dissatisfied'
               else:
                  return 'neutral or dissatisfied'
            else:
               return 'neutral or dissatisfied'
         elif obj[4] == 'Eco Plus':
            # {"feature": "Age", "instances": 1175, "metric_value": 0.3619, "depth": 4}
            if obj[2]<=37.851063829787236:
               # {"feature": "Ease of Online booking", "instances": 609, "metric_value": 0.0905, "depth": 5}
               if obj[8]>0:
                  return 'neutral or dissatisfied'
               elif obj[8]<=0:
                  return 'neutral or dissatisfied'
               else:
                  return 'neutral or dissatisfied'
            elif obj[2]>37.851063829787236:
               # {"feature": "Type of Travel", "instances": 566, "metric_value": 0.5595, "depth": 5}
               if obj[3] == 'Business travel':
                  return 'neutral or dissatisfied'
               elif obj[3] == 'Personal Travel':
                  return 'neutral or dissatisfied'
               else:
                  return 'neutral or dissatisfied'
            else:
               return 'neutral or dissatisfied'
         else:
            return 'neutral or dissatisfied'
      elif obj[6]<=0:
         # {"feature": "Ease of Online booking", "instances": 480, "metric_value": 0.0389, "depth": 3}
         if obj[8]<=1:
            return 'satisfied'
         elif obj[8]>1:
            return 'neutral or dissatisfied'
         else:
            return 'satisfied'
      else:
         return 'neutral or dissatisfied'
   else:
      return 'neutral or dissatisfied'
