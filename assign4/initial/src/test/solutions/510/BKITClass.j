.source BKITClass.java
.class public BKITClass
.super java.lang.Object
.field static a I
.field static b Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
	iconst_5
	putstatic BKITClass/a I
	ldc "string"
	putstatic BKITClass/b Ljava/lang/String;
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
.var 2 is y Ljava/lang/String; from Label0 to Label1
.var 3 is z F from Label0 to Label1
Label0:
	bipush 7
	istore_1
	ldc "x"
	astore_2
	ldc 1.5
	fstore_3
	getstatic BKITClass/a I
	iload_1
	invokestatic BKITClass/f1(II)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 4
.end method

.method public static f1(II)I
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
Label0:
	iload_0
	iload_1
	iadd
	ireturn
Label1:
.limit stack 2
.limit locals 2
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
