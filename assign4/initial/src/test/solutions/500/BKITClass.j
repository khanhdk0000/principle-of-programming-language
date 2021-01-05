.source BKITClass.java
.class public BKITClass
.super java.lang.Object
.field static a I
.field static b F

.method public static main([Ljava/lang/String;)V
	bipush 9
	putstatic BKITClass/a I
	ldc 15.7
	putstatic BKITClass/b F
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic BKITClass/a I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
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
