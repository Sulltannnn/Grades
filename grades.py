"""
برنامج تقدير درجات الطلاب
يقوم البرنامج بطلب درجة الطالب ويعرض التقدير المناسب
(ضعيف، جيد، جيد جداً، ممتاز)
يستمر البرنامج حتى يكتب المستخدم "خروج"
"""

def get_grade_rating(score):
    """
    تحويل الدرجة العددية إلى تقدير نصي
    
    المعاملات:
    score (float): درجة الطالب بين 0 و 100
    
    المخرجات:
    str: التقدير المناسب
    """
    if score < 60:
        return "ضعيف"
    elif score < 75:
        return "جيد"
    elif score < 90:
        return "جيد جداً"
    else:
        return "ممتاز"

def is_valid_score(value):
    """
    التحقق من صحة الدرجة المدخلة
    
    المعاملات:
    value (str): القيمة المدخلة من المستخدم
    
    المخرجات:
    tuple: (is_valid, score_value)
    """
    try:
        score = float(value)
        if 0 <= score <= 100:
            return True, score
        else:
            print("خطأ: الدرجة يجب أن تكون بين 0 و 100")
            return False, None
    except ValueError:
        print("خطأ: الرجاء إدخال رقم صحيح أو كلمة 'خروج'")
        return False, None

def main():
    """
    الدالة الرئيسية للبرنامج
    تتحكم في سير العمل وتفاعل المستخدم
    """
    print("=" * 40)
    print("مرحباً بك في برنامج تقدير الدرجات")
    print("أدخل درجة الطالب (0-100) أو اكتب 'خروج' لإنهاء البرنامج")
    print("=" * 40)
    
    while True:
        # طلب إدخال من المستخدم
        user_input = input("\nأدخل درجة الطالب أو 'خروج': ").strip()
        
        # التحقق من شرط الخروج
        if user_input.lower() == 'خروج':
            print("\nشكراً لاستخدام البرنامج. إلى اللقاء!")
            break
        
        # التحقق من صحة الدرجة
        valid, score = is_valid_score(user_input)
        
        if valid:
            # حساب التقدير وعرضه
            rating = get_grade_rating(score)
            print(f"الدرجة: {score} → التقدير: {rating}")

# تشغيل البرنامج
if __name__ == "__main__":
    main()
