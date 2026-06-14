-- Seed data for opportunities table
INSERT INTO opportunities (company_name, job_title, category, city, country, work_mode, required_skills, salary_min, salary_max, currency, experience_level, application_deadline, status, source_link) VALUES
-- Data Science
('Systems Limited', 'Data Scientist', 'Data Science', 'Lahore', 'Pakistan', 'Hybrid', 'Python, Pandas, Scikit-learn, SQL', 80000, 150000, 'PKR', 'Mid-Level', '2026-07-15', 'Open', 'https://systemslimited.com/careers'),
('TechVista', 'Junior Data Scientist', 'Data Science', 'Karachi', 'Pakistan', 'Onsite', 'Python, Machine Learning, Statistics', 50000, 90000, 'PKR', 'Entry-Level', '2026-07-01', 'Open', 'https://techvista.com/jobs'),
('Arbisoft', 'Senior Data Analyst', 'Data Science', 'Lahore', 'Pakistan', 'Remote', 'SQL, Python, Tableau, Power BI', 120000, 200000, 'PKR', 'Senior', '2026-06-25', 'Open', 'https://arbisoft.com/careers'),
('10Pearls', 'Data Engineer', 'Data Science', 'Islamabad', 'Pakistan', 'Hybrid', 'Python, Spark, Kafka, AWS', 100000, 180000, 'PKR', 'Mid-Level', '2026-07-20', 'Open', 'https://10pearls.com/careers'),
('Netsol Technologies', 'Business Intelligence Developer', 'Data Science', 'Lahore', 'Pakistan', 'Onsite', 'Power BI, SQL Server, DAX, Excel', 70000, 120000, 'PKR', 'Mid-Level', '2026-06-20', 'Closed', 'https://netsol.com/careers'),

-- AI
('Google', 'ML Engineer Intern', 'AI', 'Remote', 'USA', 'Remote', 'Python, TensorFlow, PyTorch, Deep Learning', 5000, 8000, 'USD', 'Entry-Level', '2026-07-30', 'Open', 'https://careers.google.com'),
('Systems Limited', 'AI/ML Developer', 'AI', 'Karachi', 'Pakistan', 'Hybrid', 'Python, TensorFlow, NLP, Computer Vision', 100000, 170000, 'PKR', 'Mid-Level', '2026-07-10', 'Open', 'https://systemslimited.com/careers'),
('Contour Software', 'AI Research Engineer', 'AI', 'Lahore', 'Pakistan', 'Onsite', 'PyTorch, Research, Deep Learning, LLMs', 130000, 220000, 'PKR', 'Senior', '2026-08-01', 'Open', 'https://contour-software.com/jobs'),
('Folio3', 'NLP Engineer', 'AI', 'Karachi', 'Pakistan', 'Remote', 'NLP, HuggingFace, Python, BERT', 90000, 160000, 'PKR', 'Mid-Level', '2026-06-28', 'Shortlisted', 'https://folio3.com/careers'),
('TechVista', 'Computer Vision Intern', 'AI', 'Islamabad', 'Pakistan', 'Onsite', 'OpenCV, Python, Deep Learning', 30000, 50000, 'PKR', 'Entry-Level', '2026-05-30', 'Expired', 'https://techvista.com/jobs'),

-- Web Development
('Arbisoft', 'React Developer', 'Web Development', 'Lahore', 'Pakistan', 'Remote', 'React, JavaScript, Node.js, REST APIs', 80000, 140000, 'PKR', 'Mid-Level', '2026-07-05', 'Open', 'https://arbisoft.com/careers'),
('10Pearls', 'Full Stack Developer', 'Web Development', 'Karachi', 'Pakistan', 'Hybrid', 'Django, React, PostgreSQL, Docker', 100000, 160000, 'PKR', 'Mid-Level', '2026-07-12', 'Open', 'https://10pearls.com/careers'),
('Netsol Technologies', 'Frontend Developer', 'Web Development', 'Lahore', 'Pakistan', 'Onsite', 'HTML, CSS, JavaScript, Vue.js', 60000, 100000, 'PKR', 'Entry-Level', '2026-06-30', 'Open', 'https://netsol.com/careers'),
('Folio3', 'Backend Developer', 'Web Development', 'Islamabad', 'Pakistan', 'Remote', 'Python, Django REST Framework, MySQL', 90000, 150000, 'PKR', 'Mid-Level', '2026-07-18', 'Open', 'https://folio3.com/careers'),
('Contour Software', 'Senior Web Developer', 'Web Development', 'Lahore', 'Pakistan', 'Hybrid', 'Node.js, TypeScript, GraphQL, AWS', 140000, 230000, 'PKR', 'Senior', '2026-06-22', 'Closed', 'https://contour-software.com/jobs'),
('Systems Limited', 'WordPress Developer', 'Web Development', 'Karachi', 'Pakistan', 'Onsite', 'WordPress, PHP, MySQL, CSS', 50000, 80000, 'PKR', 'Entry-Level', '2026-06-15', 'Expired', 'https://systemslimited.com/careers'),

-- Cyber Security
('Google', 'Security Engineer Intern', 'Cyber Security', 'Remote', 'USA', 'Remote', 'Network Security, Python, Penetration Testing', 6000, 9000, 'USD', 'Entry-Level', '2026-08-10', 'Open', 'https://careers.google.com'),
('10Pearls', 'Cyber Security Analyst', 'Cyber Security', 'Islamabad', 'Pakistan', 'Onsite', 'SIEM, Firewalls, Incident Response, ISO 27001', 90000, 160000, 'PKR', 'Mid-Level', '2026-07-25', 'Open', 'https://10pearls.com/careers'),
('Arbisoft', 'Penetration Tester', 'Cyber Security', 'Lahore', 'Pakistan', 'Hybrid', 'Kali Linux, Metasploit, Burp Suite, OWASP', 100000, 180000, 'PKR', 'Mid-Level', '2026-07-08', 'Open', 'https://arbisoft.com/careers'),
('Netsol Technologies', 'Information Security Officer', 'Cyber Security', 'Lahore', 'Pakistan', 'Onsite', 'Risk Management, Compliance, CISSP, Auditing', 150000, 250000, 'PKR', 'Senior', '2026-07-15', 'Open', 'https://netsol.com/careers'),
('TechVista', 'Security Operations Analyst', 'Cyber Security', 'Karachi', 'Pakistan', 'Remote', 'SOC, Splunk, SIEM, Threat Intelligence', 80000, 140000, 'PKR', 'Mid-Level', '2026-06-18', 'Shortlisted', 'https://techvista.com/jobs'),

-- Software Engineering
('Folio3', 'Software Engineer', 'Software Engineering', 'Karachi', 'Pakistan', 'Hybrid', 'Java, Spring Boot, Microservices, Docker', 90000, 160000, 'PKR', 'Mid-Level', '2026-07-22', 'Open', 'https://folio3.com/careers'),
('Contour Software', 'Senior Software Engineer', 'Software Engineering', 'Lahore', 'Pakistan', 'Remote', 'C++, Algorithms, System Design, Linux', 160000, 270000, 'PKR', 'Senior', '2026-08-05', 'Open', 'https://contour-software.com/jobs'),
('Systems Limited', 'Junior Software Engineer', 'Software Engineering', 'Islamabad', 'Pakistan', 'Onsite', 'Java, OOP, Git, Agile, REST APIs', 55000, 90000, 'PKR', 'Entry-Level', '2026-07-01', 'Open', 'https://systemslimited.com/careers'),
('10Pearls', 'DevOps Engineer', 'Software Engineering', 'Lahore', 'Pakistan', 'Hybrid', 'Docker, Kubernetes, CI/CD, Jenkins, AWS', 120000, 200000, 'PKR', 'Mid-Level', '2026-07-28', 'Open', 'https://10pearls.com/careers'),
('Arbisoft', 'QA Engineer', 'Software Engineering', 'Lahore', 'Pakistan', 'Remote', 'Selenium, Pytest, Test Automation, JIRA', 70000, 120000, 'PKR', 'Entry-Level', '2026-06-20', 'Closed', 'https://arbisoft.com/careers'),
('Google', 'Software Engineer Intern', 'Software Engineering', 'Remote', 'USA', 'Remote', 'Data Structures, Algorithms, Python/Java/C++', 7000, 10000, 'USD', 'Entry-Level', '2026-09-01', 'Open', 'https://careers.google.com'),
('Netsol Technologies', 'Mobile Developer', 'Software Engineering', 'Lahore', 'Pakistan', 'Onsite', 'Flutter, Dart, Firebase, REST APIs', 80000, 140000, 'PKR', 'Mid-Level', '2026-07-10', 'Open', 'https://netsol.com/careers'),
('TechVista', 'Embedded Systems Engineer', 'Software Engineering', 'Islamabad', 'Pakistan', 'Onsite', 'C, Arduino, RTOS, Firmware', 70000, 120000, 'PKR', 'Mid-Level', '2026-06-25', 'Open', 'https://techvista.com/jobs'),

-- More varied records
('Systems Limited', 'Data Science Intern', 'Data Science', 'Lahore', 'Pakistan', 'Hybrid', 'Python, Pandas, Jupyter, Statistics', 25000, 40000, 'PKR', 'Entry-Level', '2026-07-05', 'Open', 'https://systemslimited.com/careers'),
('Arbisoft', 'Cloud Data Engineer', 'Data Science', 'Remote', 'Pakistan', 'Remote', 'AWS, Redshift, Glue, Python, Airflow', 130000, 210000, 'PKR', 'Senior', '2026-08-15', 'Open', 'https://arbisoft.com/careers'),
('Folio3', 'Product Manager', 'Software Engineering', 'Karachi', 'Pakistan', 'Hybrid', 'Product Strategy, Agile, JIRA, Roadmapping', 140000, 240000, 'PKR', 'Senior', '2026-07-30', 'Open', 'https://folio3.com/careers'),
('Contour Software', 'UI/UX Designer', 'Web Development', 'Lahore', 'Pakistan', 'Remote', 'Figma, Adobe XD, User Research, Prototyping', 80000, 140000, 'PKR', 'Mid-Level', '2026-07-12', 'Open', 'https://contour-software.com/jobs'),
('10Pearls', 'Machine Learning Intern', 'AI', 'Islamabad', 'Pakistan', 'Onsite', 'Python, Scikit-learn, NumPy, Jupyter', 30000, 50000, 'PKR', 'Entry-Level', '2026-06-18', 'Expired', 'https://10pearls.com/careers'),
('Google', 'Data Analyst Intern', 'Data Science', 'Remote', 'USA', 'Remote', 'SQL, Python, Data Visualization, Statistics', 4500, 7000, 'USD', 'Entry-Level', '2026-08-20', 'Open', 'https://careers.google.com'),
('Netsol Technologies', 'Blockchain Developer', 'Software Engineering', 'Karachi', 'Pakistan', 'Remote', 'Solidity, Ethereum, Web3.js, Smart Contracts', 100000, 180000, 'PKR', 'Mid-Level', '2026-07-20', 'Open', 'https://netsol.com/careers'),
('TechVista', 'Technical Writer', 'Software Engineering', 'Islamabad', 'Pakistan', 'Remote', 'Technical Writing, Markdown, API Docs, Git', 50000, 90000, 'PKR', 'Entry-Level', '2026-07-08', 'Open', 'https://techvista.com/jobs'),
('Arbisoft', 'Cyber Security Intern', 'Cyber Security', 'Lahore', 'Pakistan', 'Hybrid', 'Networking, Linux, Security Fundamentals, Python', 25000, 45000, 'PKR', 'Entry-Level', '2026-07-15', 'Open', 'https://arbisoft.com/careers'),
('Contour Software', 'React Native Developer', 'Web Development', 'Lahore', 'Pakistan', 'Hybrid', 'React Native, JavaScript, Redux, Firebase', 90000, 160000, 'PKR', 'Mid-Level', '2026-06-30', 'Shortlisted', 'https://contour-software.com/jobs'),
('Systems Limited', 'Cloud Solutions Architect', 'Software Engineering', 'Islamabad', 'Pakistan', 'Hybrid', 'AWS, Azure, Cloud Architecture, DevOps, Python', 180000, 300000, 'PKR', 'Senior', '2026-08-01', 'Open', 'https://systemslimited.com/careers'),
('Folio3', 'AI Product Researcher', 'AI', 'Karachi', 'Pakistan', 'Remote', 'LLMs, Prompt Engineering, Python, Research', 110000, 200000, 'PKR', 'Mid-Level', '2026-07-25', 'Open', 'https://folio3.com/careers');
