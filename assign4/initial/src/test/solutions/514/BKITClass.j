.source BKITClass.java
.class public BKITClass
.super java.lang.Object
.field static a I
.field static b Ljava/lang/String;
.field static c F

.method public static main([Ljava/lang/String;)V
	iconst_5
	putstatic BKITClass/a I
	ldc "string"
	putstatic BKITClass/b Ljava/lang/String;
	ldc 5.6
	putstatic BKITClass/c F
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
.var 2 is y Ljava/lang/String; from Label0 to Label1
.var 3 is z I from Label0 to Label1
.var 4 is k F from Label0 to Label1
Label0:
	bipush 7
	istore_1
	ldc "x"
	astore_2
	iconst_2
	istore_3
	ldc 1.5
	fstore 4
	iload_1
	iconst_1
	isub
	fload 4
	invokestatic BKITClass/f1(F)I
	iadd
	istore_3
	iload_3
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 5
.end method

.method public static f1(F)I
.var 0 is x F from Label0 to Label1
Label0:
	fload_0
	invokestatic io/int_of_float(F)I
	ireturn
Label1:
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
