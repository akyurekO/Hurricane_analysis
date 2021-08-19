# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


conversion = {"M": 1000000,
              "B": 1000000000}


def updated(damages):
  updated_damages=list()
  for damage in damages:
    if damage[-1]=="M":
      converted_damage=float(damage.strip("M"))*conversion["M"]
      updated_damages.append(converted_damage)
    elif damage[-1]=="B":
      converted_damage=float(damage.strip("B"))*conversion["B"]
      updated_damages.append(converted_damage)
    else:
      updated_damages.append(damage)
  return updated_damages
updated_damages=updated(damages)
print(updated_damages)



def hurricanes_data(names,months,years,max_sustained_winds,affected_areas,damages,deaths):
  Hurricanes=dict()
  for name in names:
    index=names.index(name)
    Hurricanes[name]={"Name":names[index],"Month":months[index],"Year":years[index],"Max Sustained Wind":max_sustained_winds[index],"Areas Affected": affected_areas[index],"Damage":updated_damages[index],"Death":deaths[index]}
  return Hurricanes
   
Hurricanes_data=hurricanes_data(names,months,years,max_sustained_winds,areas_affected,damages,deaths)
print(Hurricanes_data)



def organizing_by_year(ames,months,years,max_sustained_winds,affected_areas,damages,deaths):
  Hurricane_data_by_years=dict(zip(years,list(Hurricanes_data.values())))
  return Hurricane_data_by_years

print(organizing_by_year(names,months,years,max_sustained_winds,areas_affected,damages,deaths))

def counting_damaged_areas(damaged_areas):
  areas=[]
  Damaged_areas=dict()
  for area in damaged_areas:
    for each_area in area:
      areas.append(each_area)
      Damaged_areas[each_area]=areas.count(each_area)
  return Damaged_areas

Damaged_area_frequency=counting_damaged_areas(areas_affected)
print(Damaged_area_frequency)


def maximum_hurricane_count(damaged_areas):
  dict_of_areas=counting_damaged_areas(damaged_areas)
  max_value=max(dict_of_areas.values())
  max_key=[keys for keys,value in dict_of_areas.items() if value==max_value]
  return str(max_key)+":"+str(max_value)
max_frequency=maximum_hurricane_count(areas_affected)
print(max_frequency)


def deadliest_hurricane(names,deaths):
  index=deaths.index(max(deaths))
  return str(names[index]) + ": " +str(max(deaths))+" deaths."
Deadliest=deadliest_hurricane(names,deaths)
print(Deadliest)


def hurricanes_by_mortality(deaths,names):
  mortality={0:[],1:[],2:[],3:[],4:[],5:[]}
  mortality_scale = {0: 0,1: 100,2: 500,3: 1000,4: 10000}
  
  for death in deaths:
    index=deaths.index(death)
    if death == mortality_scale[0]:
      mortality[0].append(names[index])
    elif 0<death and death <= mortality_scale[1]:
      mortality[1].append(names[index])
    elif 100 <death and death <= mortality_scale[2]:
      mortality[2].append(names[index])
    elif  500<death and death <= mortality_scale[3]:
      mortality[3].append(names[index])
    elif 1000<death and death <= mortality_scale[4]:
      mortality[4].append(names[index])
    else:
      mortality[5].append(names[index])
    
  return mortality

Hurricanes_mortality=hurricanes_by_mortality(deaths,names)
print(Hurricanes_mortality)

def hurricane_max_damage(damages,names):
  defined_damages=[]
  
  for damage in damages:
    index=damages.index(damage)
    if type(damage)==float:
      defined_damages.append(damage)
  return str(names[index])+": $"+str(max(defined_damages))

Greatest_damage=hurricane_max_damage(updated_damages,names)
print(Greatest_damage)



def rating_hurricanes_by_damage(names,damages):
  damage_scale = {0: 0,1: 100000000,2: 1000000000,3: 10000000000,4: 50000000000}
  damage_rates={0:[],1:[],2:[],3:[],4:[],5:[]}
  damage_list=[]
  for damage in damages:
    if damage != 'Damages not recorded':
      damage_list.append(float(damage))
    else:
      continue
  for damage in damage_list:
    index=damage_list.index(damage)
    if damage==damage_scale[0]:
      damage_rates[0].append(names[index])
    elif 0<damage and damage<=damage_scale[1]:
      damage_rates[1].append(names[index])
    elif 100000000<damage and damage<=damage_scale[2]:
      damage_rates[2].append(names[index])
    elif 1000000000<damage and damage<=damage_scale[3]:
      damage_rates[3].append(names[index])
    elif 10000000000<damage and damage<=damage_scale[4]:
      damage_rates[4].append(names[index])
    else:
      damage_rates[5].append(names[index])
  return damage_rates
hurricanes_damage_scale=rating_hurricanes_by_damage(names,updated_damages)
print(hurricanes_damage_scale)


