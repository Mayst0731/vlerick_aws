from pprint import pprint

from detail.format_string import format_date
from download_parse import download_site, download_json
import urllib

import requests


async def extract_details(course_list,session):
    detail_list = []
    for course in course_list:
        id = str(course['id'])
        course_link = 'https://cbecrm.stthomas.edu/web_service/services.asmx/GetProgramDetailById?id='+ id
        source = await download_json(course_link,session)
        # source = requests.get(course_link).json()
        detail = source['Program_Detail'][0]
        integrate_detail_and_course = {**detail,**course}
        instructors = integrate_detail_and_course['instructors']
        integrate_detail_and_course["course_faculties"] = await get_faculties(instructors,session)
        detail_list.append(integrate_detail_and_course)
    return detail_list


async def get_faculties(faculty_str,session):
    faculties = []
    if faculty_str is not None:
        if faculty_str == '':
            return faculties
        elif ',' not in faculty_str:
            faculty_ids = [faculty_str]
        else:
            faculty_ids = faculty_str.split(',')
        for faculty_id in faculty_ids:
            faculty_id = faculty_id.strip()
            faculty_link = 'https://cbecrm.stthomas.edu/web_service/services.asmx/GetInstructorDetailByID?id='+faculty_id
            faculty_info = await download_json(faculty_link,session)
            # faculty_info = requests.get(faculty_link).json()
            faculty = faculty_info["Instructor_Detail"][0]
            pprint(faculty)
            fac_name = faculty['name'].strip()
            faculties.append(fac_name)
    return faculties


def rename_keys(courses):
    new_courses = []
    for course in courses:
        new_course = {"name": course['marketing_name'],
                      "url": course['catalog_program_url'],
                      "category": course['marketing_topic'],
                      "category_tags":[],
                      "tuition_number": course['fee'],
                      "overview": course['current_catalog_description'],
                      "version": 1,
                      "effective_date_start":format_date(course["start_date"]),
                      "effective_date_end":format_date(course["end_date"]),
                      "credential": "",
                      "desc": course["current_catalog_description"],
                      "currency": "USD",
                      "type":course["format"],
                      "audience_title_level": '',
                      "duration_desc":"",
                      "who_attend_params": "{\"working experience\": \"\",\"background knowledge\": \"\"}",
                      "languages":"English",
                      "tuition_note":"",
                      "priority":0,
                      "publish":100,
                      "university_school":"6110_CBUS",
                      "is_advanced_management_program": False,
                      "active":True,
                      "Repeatable":"Y",
                      "course_faculties":course["course_faculties"],
                      "testimonials":[],
                      "location":"Minneapolis, MN, United States"
                      }
        if new_course["tuition_number"]!="":
            new_course["tuition_number"] = int(new_course["tuition_number"])
        if course["wioa_certified"] == True:
            new_course["credential"] = "Certificate"
        schedule = [[new_course["effective_date_start"],new_course["effective_date_end"],'','formal']]
        new_course['schedule'] = schedule
        overview = {"video_url":"",
                    "video_title":"",
                    "desc":new_course["desc"]}
        new_course["overview"] = overview
        new_courses.append(new_course)
    return new_courses


