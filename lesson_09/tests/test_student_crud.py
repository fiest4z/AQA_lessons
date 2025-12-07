from lesson_09.models import Student


def test_add_student(db):
    student = Student(
        user_id=9001,
        level="beginner",
        education_form="offline",
        subject_id=1
    )

    db.add(student)
    db.commit()

    created = db.query(Student).filter_by(user_id=9001).first()

    assert created is not None
    assert created.level == "beginner"
    assert created.education_form == "offline"

    db.delete(created)
    db.commit()


def test_update_student(db):
    student = Student(
        user_id=9002,
        level="mid",
        education_form="online",
        subject_id=2
    )

    db.add(student)
    db.commit()

    student.level = "senior"
    student.education_form = "offline"
    db.commit()

    updated = db.query(Student).filter_by(user_id=9002).first()

    assert updated.level == "senior"
    assert updated.education_form == "offline"

    db.delete(updated)
    db.commit()


def test_delete_student(db):
    student = Student(
        user_id=9003,
        level="test_level",
        education_form="test_edu",
        subject_id=3
    )

    db.add(student)
    db.commit()

    db.delete(student)
    db.commit()

    deleted = db.query(Student).filter_by(user_id=9003).first()
    assert deleted is None
