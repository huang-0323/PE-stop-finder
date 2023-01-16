library(ggplot2)
library(reshape2)

draw_pie <- function(input_dataframe){
  pdf(file = paste(piedata[1,4],"_coverage.pdf",sep = ""),width = 6,height = 6)
  legend_text <- c("Targetable","Untargetable")
  color <- c("#5eaded","#ffe0b3")
  pie(as.numeric(piedata[1,2:3]*100),
      labels = paste(round(as.numeric(piedata[1,2:3]*100),2),"%",sep = ""),
      main = paste(piedata[1,4],"_editability",sep = ""),
      col = color)
  legend("topright",legend_text,fill = color)
  dev.off()
}

args <- commandArgs(TRUE)

# draw coverage pie-chart
input_file_coverage <- paste(args[1],".coverage.summary.csv",sep = "")

coverage_summary_data <- read.csv(input_file_coverage)

for (i in 2:ncol(coverage_summary_data)) {
  piedata <- data.frame(c("exon","id","gene"),coverage_summary_data[,i],
                        1-coverage_summary_data[,i],colnames(coverage_summary_data)[i])
  names(piedata) <- c("type","target","untarget","motif")
  draw_pie(piedata)
}

# draw chromosome stack bar-chart
input_file_chromesome_coverage <- paste(args[1],".stop.summary.csv",sep = "")

chromesome_coverage_data <- read.csv(input_file_chromesome_coverage)

allchrlist <- unique(chromesome_coverage_data$chr)
for (i in 1:length(allchrlist)) {
  chr_data_tmp <- chromesome_coverage_data[chromesome_coverage_data$chr==allchrlist[i],]
  chr_data_tmp$any_edit <- apply(chr_data_tmp[,9:ncol(chr_data_tmp)], 1, any)
  chr_data_tmp_editable <- chr_data_tmp[chr_data_tmp$any_edit==T,]
  chr_id_coverage <- length(unique(chr_data_tmp_editable$id))/length(unique(chr_data_tmp$id))*100
  chr_gene_coverage <- length(unique(chr_data_tmp_editable$gene_name))/length(unique(chr_data_tmp$gene_name))*100
  chr_exon_coverage <- nrow(chr_data_tmp_editable)/nrow(chr_data_tmp)*100
  chr_coverage_result <- data.frame(c("exon","id","gene"),
                                    c(chr_exon_coverage,chr_id_coverage,chr_gene_coverage),
                                    100-c(chr_exon_coverage,chr_id_coverage,chr_gene_coverage))
  names(chr_coverage_result) <- c("type","target","untarget")
  melt(chr_coverage_result)
  chrbar_plot <- ggplot(melt(chr_coverage_result),
                        aes(x=type,y=value,fill=variable))+
    geom_bar(stat="identity",position="stack",color="black",width = 0.5)+
    theme_classic()+
    theme(axis.ticks.length.y=unit(0.2,"cm"),legend.title = element_blank(),
          axis.text= element_text(colour = "black",size = 10),
          axis.ticks.length.x=unit(0.2,"cm"))+
    scale_y_continuous(expand = c(0,0))+
    ylab("Percentage (%)")+xlab("Editing_level")+
    geom_text(aes(label=round(value,2)),vjust =0.8)
  chrbar_plot
  ggsave(paste(allchrlist[i],"_editability.pdf",sep = ""),chrbar_plot,height = 4,width = 5)
}

######test######
# i <- 2
# piedata <- data.frame(c("exon","id","gene"),coverage_summary_data[,i],
#                       1-coverage_summary_data[,i],colnames(coverage_summary_data)[i])
# names(piedata) <- c("type","target","untarget","motif")
# 
# pdf(file = paste(piedata[1,4],"_coverage.pdf",sep = ""),width = 6,height = 6)
# legend_text <- c("Targetable","Untargetable")
# color <- c("#5eaded","#ffe0b3")
# pie(as.numeric(piedata[1,2:3]*100),
#     labels = paste(round(as.numeric(piedata[1,2:3]*100),2),"%",sep = ""),
#     main = paste(piedata[1,4],"_editability",sep = ""),
#     col = color)
# legend("topright",legend_text,fill = color)
# dev.off()

