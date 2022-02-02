import asyncio
import io
import sys

import my_app


def test_sha256_print(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('test string'))
    assert my_app.calc_sha256_from_input() == 'd5579c46dfcc7f18207013e65b44e4cb4e2c2298f4ac457ba8f82743f31e930b'


def test_main(monkeypatch):
    # Lets print messages in back order
    delays = iter([5, 3, 1])

    def fake_random_generator(fake_a=1, fake_b=5):
        return next(delays)

    monkeypatch.setattr('random.randint', fake_random_generator)

    backup = sys.stdout
    sys.stdout = io.StringIO()

    asyncio.run(my_app.main())

    printed_data = sys.stdout.getvalue()
    sys.stdout.close()
    sys.stdout = backup

    assert printed_data.strip().split('\n') == ['60.000+', 'Python Developer Trainee', 'Sergey']
