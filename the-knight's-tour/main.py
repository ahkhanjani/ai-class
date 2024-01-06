import numpy as np

# با استفاده از Warnsdorff’s Rule


def knight_tour(start_x=0, start_y=0):
    # ساخت صفحه
    # خانه‌های طی تشده با -1 نشان‌گذازی می‌شوند.
    chessboard = -1 * np.ones((8, 8), dtype=int)

    # از گوشه بالا سمت چپ شروع کن
    chessboard[start_x, start_y] = 0

    if solve(chessboard, start_x, start_y, 1):
        print(chessboard)
    else:
        print("راه حلی وجود ندارد.")


# حرکات ممکن اسب در صفحه
moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
         (-2, -1), (-1, -2), (1, -2), (2, -1)]


def solve(chessboard, x, y, step):
    # اگر همه خانه‌ها بازدید شده‌اند، مسئله جل شده.
    if step == chessboard.size:
        return True

    # به ازای تمام جرکات ممکن اسب
    for move in moves:
        # محاسبه خانه بعدی
        new_x, new_y = x + move[0], y + move[1]

        if is_valid_move(chessboard, new_x, new_y):
            # اسب را در خانه قرار بده
            chessboard[new_x, new_y] = step

            # بازگشت
            if solve(chessboard, new_x, new_y, step + 1):
                return True

            # اگر راه حلی وجود نداشت، اسب را از خانه بردار (بک-ترکینگ)
            chessboard[new_x, new_y] = -1

    # اگر هیچ حرکتی به جواب نرسید
    return False


def is_valid_move(chessboard, next_x, next_y):
    # خانه مقصد نباید از صفحه بیرون بزند
    is_within_boundaries = 0 <= next_x < chessboard.shape[
        0] and 0 <= next_y < chessboard.shape[1]

    if not is_within_boundaries:
        return False

    # خانه نباید قبلاً بازدید شده باشد
    is_unvisited = chessboard[next_x, next_y] == -1

    return is_unvisited


if __name__ == "__main__":
    # نقطه شروع دلخواه را وارد کنید
    knight_tour()
