.source BKITClass.java
.class public BKITClass
.super java.lang.Object
.field static a I
.field static b I

.method public static main([Ljava/lang/String;)V
	bipush 10
	putstatic BKITClass/a I
	bipush 18
	putstatic BKITClass/b I
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic BKITClass/a I
	getstatic BKITClass/b I
	iadd
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LBKITClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
