from pprint import pprint
import matplotlib.pyplot as plt
from fhir_parser import FHIR

fhir = FHIR(endpoint="https://10.24.85.109:5001/api/", verify_ssl=False)
patients = fhir.get_all_patients()
all_observations = []
old_patients = []


def getAgingPopulation():
    for p in patients:
        if 65.0 < p.age() < 130.0:
            old_patients.append(p)
            all_observations.append(fhir.get_patient_observations(p.uuid))


def getAllObservations():
    p_obs = []
    for p in old_patients:
        p_obs.append(fhir.get_patient_observations(p.uuid))
    return p_obs


def latestObservations(all_obs, obs_type):
    latest_obs = []

    for obs_of_single_p in all_obs:
        all_obs_dt = []
        # all_obs_dt = [(obs.effective_datetime, obs.encounter_uuid) for obs in obs_of_single_p if obs_type in
        #               [component.display for component in obs.components]]
        for obs in obs_of_single_p:
            list_of_comps = [component.display for component in obs.components]
            if obs_type in list_of_comps:
                print(f"{obs_type} and {list_of_comps}: {obs.encounter_uuid}")
                all_obs_dt.append((obs.effective_datetime, obs.uuid))
        if len(all_obs_dt) > 0:
            # print(list(zip(*all_obs_dt))[1])
            latest_uuid = sorted(all_obs_dt, key=lambda tup: tup[0])[0][1]
            for obs in obs_of_single_p:
                if obs.uuid == latest_uuid:
                    latest_obs.append(obs)
                    break

    return latest_obs


def getAgeAndData(observations, obs_type):
    age_to_hr = []
    for o in observations:
        for comp in o.components:
            # print(comp.display)
            if obs_type in comp.display:
                age_to_hr.append((fhir.get_patient(o.patient_uuid).age(), comp.value))
                break
    return age_to_hr


def run():
    getAgingPopulation()
    all_obs = getAllObservations()
    stored_stuff = latestObservations(all_obs, "Body mass index (BMI) [Percentile] Per age and gender")
    agestuff = getAgeAndData(stored_stuff, "Body mass index (BMI) [Percentile] Per age and gender")
    pprint(agestuff)
    stuff = [(y,x) for (x,y) in agestuff]
    stuff = sorted(stuff, key=lambda tup: tup[0])
    pprint(stuff)
    plt.plot(*zip(*stuff))
    plt.show()


run()
