import asyncio
import re


EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@"
    r"[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
    r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$"
)


async def holehe_probiv(email: str):
    email = email.strip().lower()

    if not EMAIL_REGEX.match(email):
        return "❌ Укажите корректный email."

    try:
        process = await asyncio.create_subprocess_exec("holehe",
                                                       email,
                                                       stdout=asyncio.subprocess.PIPE,
                                                       stderr=asyncio.subprocess.PIPE,)

        stdout, stderr = await asyncio.wait_for(process.communicate(), 
                                                timeout=120)

        result = stdout.decode("utf-8", errors="ignore").strip()

        if not result:
            error = stderr.decode("utf-8", errors="ignore").strip()
            if error:
                return (f"""
                    ❌ Ошибка Holehe\n\n
                    {error[:2000]}""")
            return "❌ Holehe не вернул результатов."
        return result

    except asyncio.TimeoutError:
        try:
            process.kill()
        except Exception:
            pass
        return "⏱ Проверка заняла слишком много времени."

    except FileNotFoundError:
        return ("""
            ❌ Holehe не найден.\n\n
            Установите его командой:\n
            pip install holehe""")

    except Exception as e:
        return (f"""
            ❌ Ошибка при запуске Holehe\n\n
            {str(e)[:2000]}""")