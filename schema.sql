CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT NOT NULL,
    position TEXT NOT NULL,
    location TEXT,
    application_date TEXT NOT NULL,
    job_url TEXT,
    status TEXT NOT NULL DEFAULT 'Applied'
        CHECK (status IN ('Applied', 'Test', 'Interview', 'Rejected', 'Offer')),
    notes TEXT,
    deadline_date TEXT,
    deadline_type TEXT
);
