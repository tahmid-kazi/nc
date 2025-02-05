class TextProcessor:

    # (2/4/25)(Tue)(926-931pm) done

    # Implement method overloading for format_text method
    def format_text(self, text1: str, text2: str = None) -> str:
        if text2 == None:
            return text1.upper()
        else:
            return text1 + text2



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
