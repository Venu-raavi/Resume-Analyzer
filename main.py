from src import parser, nlp_utils, skill_extractor, matcher

def run(resume_path, job_path):
    resume_text = parser.parse_pdf(resume_path)
    job_text = parser.parse_txt(job_path)

    resume_tokens = nlp_utils.tokenize(nlp_utils.clean_text(resume_text))
    job_tokens = nlp_utils.tokenize(nlp_utils.clean_text(job_text))

    resume_skills = skill_extractor.extract_skills(resume_tokens)
    job_skills = skill_extractor.extract_skills(job_tokens)

    matched, score = matcher.match_skills(resume_skills, job_skills)

    print(f"Matched Skills: {matched}")
    print(f"Match Score: {score}%")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--resume', required=True, help='Path to the resume file')
    parser.add_argument('--job', required=True, help='Path to the job description file')
    args = parser.parse_args()
    run(args.resume, args.job)
