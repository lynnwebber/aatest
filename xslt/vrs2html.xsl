<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	version="1.0">
<xsl:output method="html"/>


<xsl:template match="/">
<html>
 <xsl:apply-templates select="raw_scores"/>
</html>
</xsl:template>

<xsl:template match="raw_scores" >
 <body>
  <table border="1">
    <xsl:apply-templates select="participant/scores/QuestandResp" />
  </table>
 </body>
</xsl:template>

<xsl:template match="scores">
 <tr>
   <td><b><xsl:value-of select="question_id" /></b></td>
   <td><xsl:value-of select="response" /></td>
 </tr>
</xsl:template>


</xsl:stylesheet>
